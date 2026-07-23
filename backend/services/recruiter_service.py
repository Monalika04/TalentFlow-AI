from backend.exceptions.custom_exceptions import (
    DuplicateResourceException,
    ResourceNotFoundException,
)

from backend.utils.enums import Status

from backend.utils.helpers import calculate_total_pages

from backend.models.recruiter_model import Recruiter
from backend.repositories.company_repository import CompanyRepository
from backend.repositories.recruiter_repository import RecruiterRepository
from backend.schemas.recruiter_schema import (
    RecruiterCreate,
    RecruiterUpdate,
)
from backend.authentication.password import hash_password

class RecruiterService:

    def __init__(self, db):
        self.repository = RecruiterRepository(db)
        self.company_repository = CompanyRepository(db)

    def create(self, request: RecruiterCreate):

        company = self.company_repository.get_by_id(request.company_id)

        if not company:
            raise ResourceNotFoundException(
    "Company not found."
)

        existing = self.repository.get_by_email(request.email)

        if existing:
            raise DuplicateResourceException(
                "Recruiter email already exists."
            )

        recruiter = Recruiter(
            company_id=request.company_id,
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            password_hash = hash_password(request.password),   # Temporary
            role=request.role,
            status=Status.ACTIVE.value,
        )

        return self.repository.create(recruiter)

    def get_by_id(self, recruiter_id: int):

        recruiter = self.repository.get_by_id(recruiter_id)

        if not recruiter:
            raise ResourceNotFoundException(
                "Recruiter not found."
            )

        return recruiter

    def search(
        self,
        page: int,
        page_size: int,
        company_id=None,
        role=None,
        status=None,
    ):

        total_records, data = self.repository.search(
            page,
            page_size,
            company_id,
            role,
            status,
        )

        return {
            "total_records": total_records,
            "total_pages": calculate_total_pages(total_records, page_size),
            "page": page,
            "page_size": page_size,
            "data": data,
        }

    def update(
        self,
        recruiter_id: int,
        request: RecruiterUpdate,
    ):

        recruiter = self.get_by_id(recruiter_id)

        for key, value in request.model_dump(exclude_unset=True).items():
            setattr(recruiter, key, value)

        return self.repository.update(recruiter)

    def delete(self, recruiter_id: int):

        recruiter = self.get_by_id(recruiter_id)

        self.repository.delete(recruiter)