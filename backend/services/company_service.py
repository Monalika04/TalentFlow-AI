from fastapi import HTTPException

from backend.models.company import Company
from backend.repositories.company_repository import CompanyRepository
from backend.schemas.company_schema import CompanyCreate


class CompanyService:

    def __init__(self, db):
        self.repository = CompanyRepository(db)

    def create_company(self, company_data: CompanyCreate):

        existing = self.repository.get_by_name(
            company_data.company_name
        )

        if existing:
            raise HTTPException(
                status_code=409,
                detail="Company already exists."
            )

        company = Company(
            company_name=company_data.company_name,
            industry=company_data.industry,
            company_size=company_data.company_size,
            headquarters=company_data.headquarters,
            website=str(company_data.website) if company_data.website else None,
            status=company_data.status
        )

        return self.repository.create_company(company)

    def get_all_companies(self):
        return self.repository.get_all()

    def get_company_by_id(self, company_id: int):

        company = self.repository.get_by_id(company_id)

        if not company:
            raise HTTPException(
                status_code=404,
                detail="Company not found."
            )

        return company

    def update_company(self, company_id: int, company_data):

        company = self.repository.get_by_id(company_id)

        if not company:
            raise HTTPException(
                status_code=404,
                detail="Company not found."
            )

        duplicate = self.repository.get_by_name(
            company_data.company_name
        )

        if duplicate and duplicate.company_id != company_id:
            raise HTTPException(
                status_code=409,
                detail="Company with this name already exists."
            )

        company.company_name = company_data.company_name
        company.industry = company_data.industry
        company.company_size = company_data.company_size
        company.headquarters = company_data.headquarters
        company.website = (
            str(company_data.website)
            if company_data.website
            else None
        )
        company.status = company_data.status

        self.repository.update_company()

        return company
    
    
    def delete_company(self, company_id: int):

        company = self.repository.get_by_id(company_id)

        if not company:
         raise HTTPException(
            status_code=404,
            detail="Company not found."
        )

        company.status = "INACTIVE"

        self.repository.delete_company()

        return {
            "message": "Company deleted successfully."
        }