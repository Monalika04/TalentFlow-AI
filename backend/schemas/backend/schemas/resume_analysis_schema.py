from datetime import datetime

from pydantic import BaseModel


class ResumeAnalysisResponse(BaseModel):

    analysis_id: int

    resume_id: int

    model_name: str

    prompt_version: str

    status: str

    execution_time_ms: float | None

    response_json: dict

    created_at: datetime

    class Config:
        from_attributes = True