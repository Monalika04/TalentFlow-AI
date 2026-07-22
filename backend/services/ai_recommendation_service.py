from math import ceil

from backend.models.ai_recommendation import AIRecommendation
from backend.repositories.ai_recommendation_repository import (
    AIRecommendationRepository,
)
from backend.repositories.application_repository import (
    ApplicationRepository,
)
from backend.schemas.ai_recommendation_schema import (
    AIRecommendationCreate,
    AIRecommendationUpdate,
    AIRecommendationListResponse,
)


class AIRecommendationService:

    def __init__(self, db):
        self.repository = AIRecommendationRepository(db)
        self.application_repository = ApplicationRepository(db)

    def create(
        self,
        request: AIRecommendationCreate,
    ):
        application = self.application_repository.get_by_id(
            request.application_id
        )

        if not application:
            raise ValueError("Application not found.")

        existing = self.repository.get_by_application_id(
            request.application_id
        )

        if existing:
            raise ValueError(
                "AI recommendation already exists for this application."
            )

        recommendation = AIRecommendation(
            application_id=request.application_id,
            overall_score=request.overall_score,
            skill_score=request.skill_score,
            experience_score=request.experience_score,
            education_score=request.education_score,
            confidence_score=request.confidence_score,
            missing_skills=request.missing_skills,
            strengths=request.strengths,
            recommendation=request.recommendation,
            reasoning=request.reasoning,
            model_version=request.model_version,
        )

        return self.repository.create(recommendation)

    def get_by_id(
        self,
        recommendation_id: int,
    ):
        recommendation = self.repository.get_by_id(
            recommendation_id
        )

        if not recommendation:
            raise ValueError(
                "AI recommendation not found."
            )

        return recommendation

    def search(
        self,
        page: int,
        page_size: int,
        application_id: int | None,
        recommendation: str | None,
        model_version: str | None,
    ):
        total, records = self.repository.search(
            page,
            page_size,
            application_id,
            recommendation,
            model_version,
        )

        return AIRecommendationListResponse(
            page=page,
            page_size=page_size,
            total_records=total,
            total_pages=ceil(total / page_size) if total else 0,
            data=records,
        )

    def update(
        self,
        recommendation_id: int,
        request: AIRecommendationUpdate,
    ):
        recommendation = self.repository.get_by_id(
            recommendation_id
        )

        if not recommendation:
            raise ValueError(
                "AI recommendation not found."
            )

        recommendation.overall_score = request.overall_score
        recommendation.skill_score = request.skill_score
        recommendation.experience_score = request.experience_score
        recommendation.education_score = request.education_score
        recommendation.confidence_score = request.confidence_score
        recommendation.missing_skills = request.missing_skills
        recommendation.strengths = request.strengths
        recommendation.recommendation = request.recommendation
        recommendation.reasoning = request.reasoning
        recommendation.model_version = request.model_version

        self.repository.update()

        return recommendation

    def delete(
        self,
        recommendation_id: int,
    ):
        recommendation = self.repository.get_by_id(
            recommendation_id
        )

        if not recommendation:
            raise ValueError(
                "AI recommendation not found."
            )

        self.repository.delete(recommendation)