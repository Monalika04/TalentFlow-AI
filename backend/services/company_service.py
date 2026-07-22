from backend.repositories.company_repository import CompanyRepository


class CompanyService:

    def __init__(self, db):

        self.repository = CompanyRepository(db)

    def get_all_companies(self):

        companies = self.repository.get_all()

        return companies