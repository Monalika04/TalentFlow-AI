from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.resume import Resume


class ResumeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, resume: Resume):

        self.db.add(resume)
        self.db.commit()
        self.db.refresh(resume)

        return resume

    def get_by_id(self, resume_id: int):

        return (
            self.db.query(Resume)
            .filter(
                Resume.resume_id == resume_id
            )
            .first()
        )

    def search(
        self,
        page: int,
        page_size: int,
        candidate_id: int | None,
        parsing_status: str | None,
        file_type: str | None,
    ):

        query = self.db.query(Resume)

        if candidate_id:
            query = query.filter(
                Resume.candidate_id == candidate_id
            )

        if parsing_status:
            query = query.filter(
                Resume.parsing_status == parsing_status
            )

        if file_type:
            query = query.filter(
                Resume.file_type == file_type
            )

        total = query.with_entities(
            func.count(Resume.resume_id)
        ).scalar()

        resumes = (
            query
            .order_by(Resume.resume_id.desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return total, resumes

    def update(self):

        self.db.commit()

    def delete(self, resume: Resume):

        self.db.delete(resume)
        self.db.commit()