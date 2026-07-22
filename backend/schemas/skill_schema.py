from pydantic import BaseModel, ConfigDict


class SkillCreate(BaseModel):
    skill_name: str
    category: str
    description: str | None = None


class SkillUpdate(BaseModel):
    skill_name: str
    category: str
    description: str | None = None
    status: str


class SkillResponse(BaseModel):
    skill_id: int
    skill_name: str
    category: str
    description: str | None = None
    status: str

    model_config = ConfigDict(from_attributes=True)


class SkillListResponse(BaseModel):
    page: int
    page_size: int
    total_records: int
    total_pages: int
    data: list[SkillResponse]