from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.job_skill import JobSkill


class JobSkillRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_job_and_skill(
        self,
        job_id: int,
        skill_id: int,
    ):
        return (
            self.db.query(JobSkill)
            .filter(
                JobSkill.job_id == job_id,
                JobSkill.skill_id == skill_id,
            )
            .first()
        )

    def create(self, job_skill: JobSkill):

        self.db.add(job_skill)
        self.db.commit()
        self.db.refresh(job_skill)

        return job_skill

    def get_by_id(self, job_skill_id: int):

        return (
            self.db.query(JobSkill)
            .filter(
                JobSkill.job_skill_id == job_skill_id
            )
            .first()
        )

    def search(
        self,
        page: int,
        page_size: int,
        job_id: int | None,
        skill_id: int | None,
        is_mandatory: bool | None,
    ):

        query = self.db.query(JobSkill)

        if job_id:
            query = query.filter(
                JobSkill.job_id == job_id
            )

        if skill_id:
            query = query.filter(
                JobSkill.skill_id == skill_id
            )

        if is_mandatory is not None:
            query = query.filter(
                JobSkill.is_mandatory == is_mandatory
            )

        total = query.with_entities(
            func.count(JobSkill.job_skill_id)
        ).scalar()

        job_skills = (
            query
            .order_by(JobSkill.job_skill_id)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return total, job_skills

    def update(self):
        self.db.commit()

    def delete(self, job_skill: JobSkill):

        self.db.delete(job_skill)
        self.db.commit()