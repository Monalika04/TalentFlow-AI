import math

from fastapi import HTTPException

from backend.models.candidate import Candidate
from backend.models.resume import Resume
from backend.repositories.resume_repository import ResumeRepository
from backend.schemas.resume_schema import (
    ResumeCreate,
    ResumeUpdate,
    ResumeListResponse,
)


class ResumeService:

    def __init__(self, db):
        self.db = db
        self.repository = ResumeRepository(db)

    def create_resume(
        self,
        data: ResumeCreate,
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

        resume = Resume(
            **data.model_dump()
        )

        return self.repository.create(resume)

    def search_resumes(
        self,
        page: int,
        page_size: int,
        candidate_id: int | None,
        parsing_status: str | None,
        file_type: str | None,
    ):

        total, resumes = self.repository.search(
            page,
            page_size,
            candidate_id,
            parsing_status,
            file_type,
        )

        return ResumeListResponse(
            page=page,
            page_size=page_size,
            total_records=total,
            total_pages=math.ceil(total / page_size)
            if total
            else 0,
            data=resumes,
        )

    def get_resume_by_id(
        self,
        resume_id: int,
    ):

        resume = self.repository.get_by_id(resume_id)

        if not resume:
            raise HTTPException(
                status_code=404,
                detail="Resume not found."
            )

        return resume

    def update_resume(
        self,
        resume_id: int,
        data: ResumeUpdate,
    ):

        resume = self.repository.get_by_id(resume_id)

        if not resume:
            raise HTTPException(
                status_code=404,
                detail="Resume not found."
            )

        resume.file_name = data.file_name
        resume.file_path = data.file_path
        resume.file_type = data.file_type
        resume.file_size_kb = data.file_size_kb
        resume.resume_version = data.resume_version
        resume.parsing_status = data.parsing_status
        resume.ai_summary = data.ai_summary

        self.repository.update()

        return resume

    def delete_resume(
        self,
        resume_id: int,
    ):

        resume = self.repository.get_by_id(resume_id)

        if not resume:
            raise HTTPException(
                status_code=404,
                detail="Resume not found."
            )

        self.repository.delete(resume)

        return {
            "message": "Resume deleted successfully."
        }