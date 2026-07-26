from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from backend.models.candidate import Candidate


class CandidateRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):

        return (
            self.db.query(Candidate)
            .filter(Candidate.email == email)
            .first()
        )

    def get_by_phone(self, phone: str):

        return (
            self.db.query(Candidate)
            .filter(Candidate.phone == phone)
            .first()
        )

    def get_by_id(self, candidate_id: int):

        return (
            self.db.query(Candidate)
            .filter(Candidate.candidate_id == candidate_id)
            .first()
        )

    def create(self, candidate: Candidate):

        self.db.add(candidate)
        self.db.commit()
        self.db.refresh(candidate)

        return candidate

    def update(self, candidate: Candidate):

        self.db.commit()
        self.db.refresh(candidate)

        return candidate

    def delete(self, candidate: Candidate):

        self.db.delete(candidate)
        self.db.commit()

    def search(
        self,
        page: int,
        page_size: int,
        city: str | None,
        status: str | None,
        search: str | None,
    ):

        query = self.db.query(Candidate)

        if city:
            query = query.filter(Candidate.city == city)

        if status:
            query = query.filter(Candidate.status == status)

        if search:
            query = query.filter(
                or_(
                    Candidate.first_name.ilike(f"%{search}%"),
                    Candidate.last_name.ilike(f"%{search}%"),
                    Candidate.email.ilike(f"%{search}%"),
                )
            )

        total = query.with_entities(
            func.count(Candidate.candidate_id)
        ).scalar()

        candidates = (
            query
            .order_by(Candidate.candidate_id)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return total, candidates