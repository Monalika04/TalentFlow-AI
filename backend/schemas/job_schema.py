from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class JobCreate(BaseModel):
    company_id: int
    job_title: str
    department: str
    job_description: str
    location: str
    employment_type: str
    min_experience: Decimal
    max_experience: Decimal
    min_salary: Decimal
    max_salary: Decimal
    vacancies: int = 1


class JobUpdate(BaseModel):
    company_id: int
    job_title: str
    department: str
    job_description: str
    location: str
    employment_type: str
    min_experience: Decimal
    max_experience: Decimal
    min_salary: Decimal
    max_salary: Decimal
    vacancies: int
    status: str


class JobResponse(BaseModel):
    job_id: int
    company_id: int
    job_title: str
    department: str
    job_description: str
    location: str
    employment_type: str
    min_experience: Decimal
    max_experience: Decimal
    min_salary: Decimal
    max_salary: Decimal
    vacancies: int
    status: str

    model_config = ConfigDict(from_attributes=True)


class JobListResponse(BaseModel):
    page: int
    page_size: int
    total_records: int
    total_pages: int
    data: list[JobResponse]