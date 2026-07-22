import math

from fastapi import HTTPException

from backend.models.application import Application
from backend.models.candidate import Candidate
from backend.models.job import Job
from backend.repositories.application_repository import ApplicationRepository
from backend.schemas.application_schema import (
    ApplicationCreate,
    ApplicationUpdate,
    ApplicationListResponse,
)


class ApplicationService:

    def __init__(self, db):
        self.db = db
        self.repository = ApplicationRepository(db)

    def create_application(
        self,
        data: ApplicationCreate,
    ):

        candidate = (
            self.db.query(Candidate)
            .filter(
                Candidate.candidate_id == data.candidate_id
            )
            .first()
        )

        if not candidate:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found."
            )

        job = (
            self.db.query(Job)
            .filter(
                Job.job_id == data.job_id
            )
            .first()
        )

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        duplicate = self.repository.get_by_candidate_and_job(
            data.candidate_id,
            data.job_id,
        )

        if duplicate:
            raise HTTPException(
                status_code=409,
                detail="Candidate has already applied for this job."
            )

        application = Application(
            **data.model_dump()
        )

        return self.repository.create(application)

    def search_applications(
        self,
        page: int,
        page_size: int,
        candidate_id: int | None,
        job_id: int | None,
        application_status: str | None,
    ):

        total, applications = self.repository.search(
            page,
            page_size,
            candidate_id,
            job_id,
            application_status,
        )

        return ApplicationListResponse(
            page=page,
            page_size=page_size,
            total_records=total,
            total_pages=math.ceil(total / page_size)
            if total
            else 0,
            data=applications,
        )

    def get_application_by_id(
        self,
        application_id: int,
    ):

        application = self.repository.get_by_id(
            application_id
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        return application

    def update_application(
        self,
        application_id: int,
        data: ApplicationUpdate,
    ):

        application = self.repository.get_by_id(
            application_id
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        application.application_status = data.application_status
        application.ai_match_score = data.ai_match_score
        application.recruiter_notes = data.recruiter_notes
        application.source = data.source

        self.repository.update()

        return application

    def delete_application(
        self,
        application_id: int,
    ):

        application = self.repository.get_by_id(
            application_id
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        self.repository.delete(application)

        return {
            "message": "Application deleted successfully."
        }