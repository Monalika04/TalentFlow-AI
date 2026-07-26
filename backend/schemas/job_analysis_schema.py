from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class JobAnalysisResponse(BaseModel):

    analysis_id: int
    job_id: int

    model_name: str
    prompt_version: str

    analysis_version: int

    status: str

    execution_time_ms: float | None

    ai_response_json: dict[str, Any]

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )