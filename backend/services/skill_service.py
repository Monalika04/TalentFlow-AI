import math

from fastapi import HTTPException

from backend.models.skill import Skill
from backend.repositories.skill_repository import SkillRepository
from backend.schemas.skill_schema import (
    SkillCreate,
    SkillUpdate,
    SkillListResponse,
)


class SkillService:

    def __init__(self, db):
        self.repository = SkillRepository(db)

    def create_skill(self, data: SkillCreate):

        if self.repository.get_by_name(data.skill_name):
            raise HTTPException(
                status_code=409,
                detail="Skill already exists."
            )

        skill = Skill(**data.model_dump())

        return self.repository.create(skill)

    def search_skills(
        self,
        page: int,
        page_size: int,
        category: str | None,
        status: str | None,
        search: str | None,
    ):

        total, skills = self.repository.search(
            page,
            page_size,
            category,
            status,
            search,
        )

        return SkillListResponse(
            page=page,
            page_size=page_size,
            total_records=total,
            total_pages=math.ceil(total / page_size)
            if total else 0,
            data=skills,
        )

    def get_skill_by_id(self, skill_id: int):

        skill = self.repository.get_by_id(skill_id)

        if not skill:
            raise HTTPException(
                status_code=404,
                detail="Skill not found."
            )

        return skill

    def update_skill(
        self,
        skill_id: int,
        data: SkillUpdate,
    ):

        skill = self.repository.get_by_id(skill_id)

        if not skill:
            raise HTTPException(
                status_code=404,
                detail="Skill not found."
            )

        duplicate = self.repository.get_by_name(data.skill_name)

        if (
            duplicate
            and duplicate.skill_id != skill_id
        ):
            raise HTTPException(
                status_code=409,
                detail="Skill already exists."
            )

        skill.skill_name = data.skill_name
        skill.category = data.category
        skill.description = data.description
        skill.status = data.status

        self.repository.update()

        return skill

    def delete_skill(self, skill_id: int):

        skill = self.repository.get_by_id(skill_id)

        if not skill:
            raise HTTPException(
                status_code=404,
                detail="Skill not found."
            )

        skill.status = "INACTIVE"

        self.repository.delete()

        return {
            "message": "Skill deleted successfully."
        }