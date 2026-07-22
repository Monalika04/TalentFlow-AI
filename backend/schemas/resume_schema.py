from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ResumeCreate(BaseModel):
    candidate_id: int
    file_name: str
    file_path: str
    file_type: str
    file_size_kb: Decimal
    resume_version: int = 1


class ResumeUpdate(BaseModel):
    file_name: str
    file_path: str
    file_type: str
    file_size_kb: Decimal
    resume_version: int
    parsing_status: str
    ai_summary: str | None = None


class ResumeResponse(BaseModel):
    resume_id: int
    candidate_id: int
    file_name: str
    file_path: str
    file_type: str
    file_size_kb: Decimal
    resume_version: int
    upload_date: datetime
    parsing_status: str
    ai_summary: str | None
    
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ResumeListResponse(BaseModel):
    page: int
    page_size: int
    total_records: int
    total_pages: int
    data: list[ResumeResponse]