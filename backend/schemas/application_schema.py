from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ApplicationCreate(BaseModel):
    candidate_id: int
    job_id: int
    source: str | None = None


class ApplicationUpdate(BaseModel):
    application_status: str
    ai_match_score: Decimal | None = None
    recruiter_notes: str | None = None
    source: str | None = None


class ApplicationResponse(BaseModel):
    application_id: int
    candidate_id: int
    job_id: int
    application_date: datetime
    application_status: str
    ai_match_score: Decimal | None
    recruiter_notes: str | None
    source: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ApplicationListResponse(BaseModel):
    page: int
    page_size: int
    total_records: int
    total_pages: int
    data: list[ApplicationResponse]