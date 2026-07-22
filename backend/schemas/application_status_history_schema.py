from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ApplicationStatusHistoryCreate(BaseModel):
    application_id: int
    previous_status: str | None = None
    new_status: str
    changed_by: str
    remarks: str | None = None


class ApplicationStatusHistoryUpdate(BaseModel):
    changed_by: str
    remarks: str | None = None


class ApplicationStatusHistoryResponse(BaseModel):
    history_id: int
    application_id: int
    previous_status: str | None
    new_status: str
    changed_by: str
    changed_at: datetime
    remarks: str | None

    model_config = ConfigDict(from_attributes=True)


class ApplicationStatusHistoryListResponse(BaseModel):
    page: int
    page_size: int
    total_records: int
    total_pages: int
    data: list[ApplicationStatusHistoryResponse]