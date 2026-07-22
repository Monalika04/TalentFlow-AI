from sqlalchemy.orm import Session

from backend.models.company import Company


class CompanyRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_company(self, company: Company):
        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)
        return company

    def get_all(self):
        return (
            self.db.query(Company)
            .order_by(Company.company_name)
            .all()
        )

    def get_by_id(self, company_id: int):
        return (
            self.db.query(Company)
            .filter(Company.company_id == company_id)
            .first()
        )

    def get_by_name(self, company_name: str):
        return (
            self.db.query(Company)
            .filter(Company.company_name == company_name)
            .first()
        )

    def update_company(self):
        self.db.commit()
        
    def delete_company(self):
        self.db.commit()

