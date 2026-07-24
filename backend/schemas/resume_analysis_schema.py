from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class ResumeAnalysisResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    analysis_id: int
    resume_id: int

    model_name: str
    prompt_version: str
    analysis_version: int

    status: str

    execution_time_ms: float | None

    facts: dict[str, Any]

    intelligence: dict[str, Any]

    created_at: datetime
    updated_at: datetime