from sqlalchemy.orm import Session

from backend.models.recruiter_model import Recruiter


class RecruiterRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, recruiter: Recruiter) -> Recruiter:
        self.db.add(recruiter)
        self.db.commit()
        self.db.refresh(recruiter)
        return recruiter

    def get_by_id(self, recruiter_id: int) -> Recruiter | None:
        return (
            self.db.query(Recruiter)
            .filter(Recruiter.recruiter_id == recruiter_id)
            .first()
        )

    def get_by_email(self, email: str) -> Recruiter | None:
        return (
            self.db.query(Recruiter)
            .filter(Recruiter.email == email)
            .first()
        )

    def search(
        self,
        page: int,
        page_size: int,
        company_id: int | None = None,
        role: str | None = None,
        status: str | None = None,
    ):
        query = self.db.query(Recruiter)

        if company_id:
            query = query.filter(Recruiter.company_id == company_id)

        if role:
            query = query.filter(Recruiter.role == role)

        if status:
            query = query.filter(Recruiter.status == status)

        total_records = query.count()

        recruiters = (
            query.offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return total_records, recruiters

    def update(self, recruiter: Recruiter) -> Recruiter:
        self.db.commit()
        self.db.refresh(recruiter)
        return recruiter

    def delete(self, recruiter: Recruiter):
        self.db.delete(recruiter)
        self.db.commit()