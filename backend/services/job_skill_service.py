import math

from fastapi import HTTPException

from backend.models.job import Job
from backend.models.skill import Skill
from backend.models.job_skill import JobSkill
from backend.repositories.job_skill_repository import JobSkillRepository
from backend.schemas.job_skill_schema import (
    JobSkillCreate,
    JobSkillUpdate,
    JobSkillListResponse,
)


class JobSkillService:

    def __init__(self, db):
        self.db = db
        self.repository = JobSkillRepository(db)

    def create_job_skill(
        self,
        data: JobSkillCreate,
    ):

        job = (
            self.db.query(Job)
            .filter(Job.job_id == data.job_id)
            .first()
        )

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
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

        duplicate = self.repository.get_by_job_and_skill(
            data.job_id,
            data.skill_id,
        )

        if duplicate:
            raise HTTPException(
                status_code=409,
                detail="Job already has this skill."
            )

        job_skill = JobSkill(
            **data.model_dump()
        )

        return self.repository.create(job_skill)

    def search_job_skills(
        self,
        page: int,
        page_size: int,
        job_id: int | None,
        skill_id: int | None,
        is_mandatory: bool | None,
    ):

        total, job_skills = self.repository.search(
            page,
            page_size,
            job_id,
            skill_id,
            is_mandatory,
        )

        return JobSkillListResponse(
            page=page,
            page_size=page_size,
            total_records=total,
            total_pages=math.ceil(total / page_size)
            if total
            else 0,
            data=job_skills,
        )

    def get_job_skill_by_id(
        self,
        job_skill_id: int,
    ):

        job_skill = self.repository.get_by_id(
            job_skill_id
        )

        if not job_skill:
            raise HTTPException(
                status_code=404,
                detail="Job skill not found."
            )

        return job_skill

    def update_job_skill(
        self,
        job_skill_id: int,
        data: JobSkillUpdate,
    ):

        job_skill = self.repository.get_by_id(
            job_skill_id
        )

        if not job_skill:
            raise HTTPException(
                status_code=404,
                detail="Job skill not found."
            )

        job_skill.importance_weight = data.importance_weight
        job_skill.is_mandatory = data.is_mandatory

        self.repository.update()

        return job_skill

    def delete_job_skill(
        self,
        job_skill_id: int,
    ):

        job_skill = self.repository.get_by_id(
            job_skill_id
        )

        if not job_skill:
            raise HTTPException(
                status_code=404,
                detail="Job skill not found."
            )

        self.repository.delete(job_skill)

        return {
            "message": "Job skill deleted successfully."
        }