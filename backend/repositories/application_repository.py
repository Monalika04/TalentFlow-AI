from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.application import Application


class ApplicationRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_candidate_and_job(
        self,
        candidate_id: int,
        job_id: int,
    ):
        return (
            self.db.query(Application)
            .filter(
                Application.candidate_id == candidate_id,
                Application.job_id == job_id,
            )
            .first()
        )

    def create(
        self,
        application: Application,
    ):
        self.db.add(application)
        self.db.commit()
        self.db.refresh(application)

        return application

    def get_by_id(
        self,
        application_id: int,
    ):
        return (
            self.db.query(Application)
            .filter(
                Application.application_id == application_id
            )
            .first()
        )

    def search(
        self,
        page: int,
        page_size: int,
        candidate_id: int | None,
        job_id: int | None,
        application_status: str | None,
    ):
        query = self.db.query(Application)

        if candidate_id:
            query = query.filter(
                Application.candidate_id == candidate_id
            )

        if job_id:
            query = query.filter(
                Application.job_id == job_id
            )

        if application_status:
            query = query.filter(
                Application.application_status == application_status
            )

        total = query.with_entities(
            func.count(Application.application_id)
        ).scalar()

        applications = (
            query
            .order_by(Application.application_id.desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return total, applications

    def update(self):
        self.db.commit()

    def delete(
        self,
        application: Application,
    ):
        self.db.delete(application)
        self.db.commit()