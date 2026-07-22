from pydantic import BaseModel, ConfigDict


class JobSkillCreate(BaseModel):
    job_id: int
    skill_id: int
    importance_weight: int = 3
    is_mandatory: bool = False


class JobSkillUpdate(BaseModel):
    importance_weight: int
    is_mandatory: bool


class JobSkillResponse(BaseModel):
    job_skill_id: int
    job_id: int
    skill_id: int
    importance_weight: int
    is_mandatory: bool

    model_config = ConfigDict(from_attributes=True)


class JobSkillListResponse(BaseModel):
    page: int
    page_size: int
    total_records: int
    total_pages: int
    data: list[JobSkillResponse]