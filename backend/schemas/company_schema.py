from decimal import Decimal

from pydantic import BaseModel, EmailStr, HttpUrl


class CompanyCreate(BaseModel):
    company_name: str
    industry: str
    company_size: str | None = None
    headquarters: str | None = None
    website: HttpUrl | None = None
    status: str = "ACTIVE"


class CompanyUpdate(BaseModel):
    company_name: str
    industry: str
    company_size: str | None = None
    headquarters: str | None = None
    website: HttpUrl | None = None
    status: str


class CompanyResponse(BaseModel):
    company_id: int
    company_name: str
    industry: str
    company_size: str | None = None
    headquarters: str | None = None
    website: str | None = None
    status: str

    class Config:
        from_attributes = True


class CandidateUpdate(BaseModel):
    first_name: str
    last_name: str

    email: EmailStr
    phone: str

    city: str
    state: str
    country: str

    total_experience: Decimal

    current_ctc: Decimal
    expected_ctc: Decimal

    notice_period_days: int

    highest_education: str

    linkedin_url: str | None = None
    github_url: str | None = None
    portfolio_url: str | None = None

    status: str

    class Config:
        from_attributes = True