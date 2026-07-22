from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.job import Job


class JobRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, job: Job):

        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)

        return job

    def get_by_id(self, job_id: int):

        return (
            self.db.query(Job)
            .filter(Job.job_id == job_id)
            .first()
        )

    def search(
        self,
        page: int,
        page_size: int,
        company_id: int | None,
        department: str | None,
        status: str | None,
        employment_type: str | None,
        search: str | None,
    ):

        query = self.db.query(Job)

        if company_id:
            query = query.filter(Job.company_id == company_id)

        if department:
            query = query.filter(Job.department == department)

        if status:
            query = query.filter(Job.status == status)

        if employment_type:
            query = query.filter(
                Job.employment_type == employment_type
            )

        if search:
            query = query.filter(
                Job.job_title.ilike(f"%{search}%")
            )

        total = query.with_entities(
            func.count(Job.job_id)
        ).scalar()

        jobs = (
            query
            .order_by(Job.job_title)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return total, jobs

    def update(self):
        self.db.commit()

    def delete(self):
        self.db.commit()