from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RecruiterCreate(BaseModel):
    company_id: int
    first_name: str
    last_name: str
    email: str
    password: str
    role: str


class RecruiterUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    role: str | None = None
    status: str | None = None


class RecruiterResponse(BaseModel):
    recruiter_id: int
    company_id: int
    first_name: str
    last_name: str
    email: str
    role: str
    status: str
    last_login: datetime | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RecruiterListResponse(BaseModel):
    total_records: int
    total_pages: int
    page: int
    page_size: int
    data: list[RecruiterResponse]