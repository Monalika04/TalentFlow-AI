from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class CandidateSkillCreate(BaseModel):
    candidate_id: int
    skill_id: int
    proficiency_level: str
    years_experience: Decimal = Decimal("0.0")
    last_used: date | None = None
    is_primary: bool = False


class CandidateSkillUpdate(BaseModel):
    proficiency_level: str
    years_experience: Decimal
    last_used: date | None = None
    is_primary: bool


class CandidateSkillResponse(BaseModel):
    candidate_skill_id: int
    candidate_id: int
    skill_id: int
    proficiency_level: str
    years_experience: Decimal
    last_used: date | None = None
    is_primary: bool

    model_config = ConfigDict(from_attributes=True)


class CandidateSkillListResponse(BaseModel):
    page: int
    page_size: int
    total_records: int
    total_pages: int
    data: list[CandidateSkillResponse]