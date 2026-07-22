from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class AIRecommendationCreate(BaseModel):
    application_id: int
    overall_score: Decimal
    skill_score: Decimal
    experience_score: Decimal
    education_score: Decimal
    confidence_score: Decimal
    missing_skills: str | None = None
    strengths: str | None = None
    recommendation: str
    reasoning: str | None = None
    model_version: str


class AIRecommendationUpdate(BaseModel):
    overall_score: Decimal
    skill_score: Decimal
    experience_score: Decimal
    education_score: Decimal
    confidence_score: Decimal
    missing_skills: str | None = None
    strengths: str | None = None
    recommendation: str
    reasoning: str | None = None
    model_version: str


class AIRecommendationResponse(BaseModel):
    recommendation_id: int
    application_id: int
    overall_score: Decimal
    skill_score: Decimal
    experience_score: Decimal
    education_score: Decimal
    confidence_score: Decimal
    missing_skills: str | None
    strengths: str | None
    recommendation: str
    reasoning: str | None
    model_version: str
    generated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AIRecommendationListResponse(BaseModel):
    page: int
    page_size: int
    total_records: int
    total_pages: int
    data: list[AIRecommendationResponse]