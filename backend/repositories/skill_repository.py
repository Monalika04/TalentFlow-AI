from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.skill import Skill


class SkillRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_name(self, skill_name: str):

        return (
            self.db.query(Skill)
            .filter(Skill.skill_name == skill_name)
            .first()
        )

    def create(self, skill: Skill):

        self.db.add(skill)
        self.db.commit()
        self.db.refresh(skill)

        return skill

    def get_by_id(self, skill_id: int):

        return (
            self.db.query(Skill)
            .filter(Skill.skill_id == skill_id)
            .first()
        )

    def search(
        self,
        page: int,
        page_size: int,
        category: str | None,
        status: str | None,
        search: str | None,
    ):

        query = self.db.query(Skill)

        if category:
            query = query.filter(Skill.category == category)

        if status:
            query = query.filter(Skill.status == status)

        if search:
            query = query.filter(
                Skill.skill_name.ilike(f"%{search}%")
            )

        total = query.with_entities(
            func.count(Skill.skill_id)
        ).scalar()

        skills = (
            query
            .order_by(Skill.skill_name)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return total, skills

    def update(self):
        self.db.commit()

    def delete(self):
        self.db.commit()