import math

from fastapi import HTTPException

from backend.models.company import Company
from backend.models.job import Job
from backend.repositories.job_repository import JobRepository
from backend.schemas.job_schema import (
    JobCreate,
    JobUpdate,
    JobListResponse,
)


class JobService:

    def __init__(self, db):
        self.db = db
        self.repository = JobRepository(db)

    def create_job(
        self,
        data: JobCreate,
    ):

        company = (
            self.db.query(Company)
            .filter(Company.company_id == data.company_id)
            .first()
        )

        if not company:
            raise HTTPException(
                status_code=404,
                detail="Company not found."
            )

        job = Job(**data.model_dump())

        return self.repository.create(job)

    def search_jobs(
        self,
        page: int,
        page_size: int,
        company_id: int | None,
        department: str | None,
        status: str | None,
        employment_type: str | None,
        search: str | None,
    ):

        total, jobs = self.repository.search(
            page,
            page_size,
            company_id,
            department,
            status,
            employment_type,
            search,
        )

        return JobListResponse(
            page=page,
            page_size=page_size,
            total_records=total,
            total_pages=math.ceil(total / page_size)
            if total
            else 0,
            data=jobs,
        )

    def get_job_by_id(
        self,
        job_id: int,
    ):

        job = self.repository.get_by_id(job_id)

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        return job

    def update_job(
        self,
        job_id: int,
        data: JobUpdate,
    ):

        job = self.repository.get_by_id(job_id)

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        company = (
            self.db.query(Company)
            .filter(Company.company_id == data.company_id)
            .first()
        )

        if not company:
            raise HTTPException(
                status_code=404,
                detail="Company not found."
            )

        job.company_id = data.company_id
        job.job_title = data.job_title
        job.department = data.department
        job.job_description = data.job_description
        job.location = data.location
        job.employment_type = data.employment_type
        job.min_experience = data.min_experience
        job.max_experience = data.max_experience
        job.min_salary = data.min_salary
        job.max_salary = data.max_salary
        job.vacancies = data.vacancies
        job.status = data.status

        self.repository.update()

        return job

    def delete_job(
        self,
        job_id: int,
    ):

        job = self.repository.get_by_id(job_id)

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        job.status = "CLOSED"

        self.repository.delete()

        return {
            "message": "Job closed successfully."
        }