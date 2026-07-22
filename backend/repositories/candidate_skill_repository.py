from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.candidate_skill import CandidateSkill


class CandidateSkillRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_candidate_and_skill(
        self,
        candidate_id: int,
        skill_id: int,
    ):
        return (
            self.db.query(CandidateSkill)
            .filter(
                CandidateSkill.candidate_id == candidate_id,
                CandidateSkill.skill_id == skill_id,
            )
            .first()
        )

    def create(self, candidate_skill: CandidateSkill):

        self.db.add(candidate_skill)
        self.db.commit()
        self.db.refresh(candidate_skill)

        return candidate_skill

    def get_by_id(self, candidate_skill_id: int):

        return (
            self.db.query(CandidateSkill)
            .filter(
                CandidateSkill.candidate_skill_id == candidate_skill_id
            )
            .first()
        )

    def search(
        self,
        page: int,
        page_size: int,
        candidate_id: int | None,
        skill_id: int | None,
        proficiency_level: str | None,
    ):

        query = self.db.query(CandidateSkill)

        if candidate_id:
            query = query.filter(
                CandidateSkill.candidate_id == candidate_id
            )

        if skill_id:
            query = query.filter(
                CandidateSkill.skill_id == skill_id
            )

        if proficiency_level:
            query = query.filter(
                CandidateSkill.proficiency_level == proficiency_level
            )

        total = query.with_entities(
            func.count(CandidateSkill.candidate_skill_id)
        ).scalar()

        candidate_skills = (
            query
            .order_by(CandidateSkill.candidate_skill_id)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return total, candidate_skills

    def update(self):
        self.db.commit()

    def delete(self, candidate_skill: CandidateSkill):

        self.db.delete(candidate_skill)
        self.db.commit()