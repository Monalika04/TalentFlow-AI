from decimal import Decimal

from pydantic import BaseModel, ConfigDict, EmailStr


class CandidateCreate(BaseModel):

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


class CandidateResponse(CandidateCreate):

    candidate_id: int
    status: str

    model_config = ConfigDict(from_attributes=True)


class CandidateListResponse(BaseModel):

    page: int
    page_size: int
    total_records: int
    total_pages: int

    data: list[CandidateResponse]