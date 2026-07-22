from sqlalchemy.orm import Session

from backend.models.company import Company


class CompanyRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):

        return (
            self.db
            .query(Company)
            .all()
        )