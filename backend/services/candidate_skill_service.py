import math

from fastapi import HTTPException

from backend.models.candidate import Candidate
from backend.models.skill import Skill
from backend.models.candidate_skill import CandidateSkill
from backend.repositories.candidate_skill_repository import CandidateSkillRepository
from backend.schemas.candidate_skill_schema import (
    CandidateSkillCreate,
    CandidateSkillUpdate,
    CandidateSkillListResponse,
)


class CandidateSkillService:

    def __init__(self, db):
        self.db = db
        self.repository = CandidateSkillRepository(db)

    def create_candidate_skill(
        self,
        data: CandidateSkillCreate,
    ):

        candidate = (
            self.db.query(Candidate)
            .filter(Candidate.candidate_id == data.candidate_id)
            .first()
        )

        if not candidate:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found."
            )

        skill = (
            self.db.query(Skill)
            .filter(Skill.skill_id == data.skill_id)
            .first()
        )

        if not skill:
            raise HTTPException(
                status_code=404,
                detail="Skill not found."
            )

        duplicate = self.repository.get_by_candidate_and_skill(
            data.candidate_id,
            data.skill_id,
        )

        if duplicate:
            raise HTTPException(
                status_code=409,
                detail="Candidate already has this skill."
            )

        candidate_skill = CandidateSkill(
            **data.model_dump()
        )

        return self.repository.create(candidate_skill)

    def search_candidate_skills(
        self,
        page: int,
        page_size: int,
        candidate_id: int | None,
        skill_id: int | None,
        proficiency_level: str | None,
    ):

        total, candidate_skills = self.repository.search(
            page,
            page_size,
            candidate_id,
            skill_id,
            proficiency_level,
        )

        return CandidateSkillListResponse(
            page=page,
            page_size=page_size,
            total_records=total,
            total_pages=math.ceil(total / page_size)
            if total
            else 0,
            data=candidate_skills,
        )

    def get_candidate_skill_by_id(
        self,
        candidate_skill_id: int,
    ):

        candidate_skill = self.repository.get_by_id(
            candidate_skill_id
        )

        if not candidate_skill:
            raise HTTPException(
                status_code=404,
                detail="Candidate skill not found."
            )

        return candidate_skill

    def update_candidate_skill(
        self,
        candidate_skill_id: int,
        data: CandidateSkillUpdate,
    ):

        candidate_skill = self.repository.get_by_id(
            candidate_skill_id
        )

        if not candidate_skill:
            raise HTTPException(
                status_code=404,
                detail="Candidate skill not found."
            )

        candidate_skill.proficiency_level = data.proficiency_level
        candidate_skill.years_experience = data.years_experience
        candidate_skill.last_used = data.last_used
        candidate_skill.is_primary = data.is_primary

        self.repository.update()

        return candidate_skill

    def delete_candidate_skill(
        self,
        candidate_skill_id: int,
    ):

        candidate_skill = self.repository.get_by_id(
            candidate_skill_id
        )

        if not candidate_skill:
            raise HTTPException(
                status_code=404,
                detail="Candidate skill not found."
            )

        self.repository.delete(candidate_skill)

        return {
            "message": "Candidate skill deleted successfully."
        }