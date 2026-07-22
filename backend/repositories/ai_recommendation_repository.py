from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.ai_recommendation import AIRecommendation


class AIRecommendationRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        recommendation: AIRecommendation,
    ):
        self.db.add(recommendation)
        self.db.commit()
        self.db.refresh(recommendation)

        return recommendation

    def get_by_id(
        self,
        recommendation_id: int,
    ):
        return (
            self.db.query(AIRecommendation)
            .filter(
                AIRecommendation.recommendation_id == recommendation_id
            )
            .first()
        )

    def get_by_application_id(
        self,
        application_id: int,
    ):
        return (
            self.db.query(AIRecommendation)
            .filter(
                AIRecommendation.application_id == application_id
            )
            .first()
        )

    def search(
        self,
        page: int,
        page_size: int,
        application_id: int | None,
        recommendation: str | None,
        model_version: str | None,
    ):
        query = self.db.query(AIRecommendation)

        if application_id:
            query = query.filter(
                AIRecommendation.application_id == application_id
            )

        if recommendation:
            query = query.filter(
                AIRecommendation.recommendation == recommendation
            )

        if model_version:
            query = query.filter(
                AIRecommendation.model_version == model_version
            )

        total = query.with_entities(
            func.count(AIRecommendation.recommendation_id)
        ).scalar()

        recommendations = (
            query
            .order_by(
                AIRecommendation.generated_at.desc()
            )
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return total, recommendations

    def update(self):
        self.db.commit()

    def delete(
        self,
        recommendation: AIRecommendation,
    ):
        self.db.delete(recommendation)
        self.db.commit()