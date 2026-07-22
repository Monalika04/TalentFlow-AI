from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from backend.dependencies.database import get_db
from backend.schemas.ai_recommendation_schema import (
    AIRecommendationCreate,
    AIRecommendationUpdate,
    AIRecommendationResponse,
    AIRecommendationListResponse,
)
from backend.services.ai_recommendation_service import (
    AIRecommendationService,
)

router = APIRouter(
    prefix="/ai-recommendations",
    tags=["AI Recommendations"],
)


@router.post(
    "/",
    response_model=AIRecommendationResponse,
)
def create_recommendation(
    request: AIRecommendationCreate,
    db: Session = Depends(get_db),
):
    try:
        service = AIRecommendationService(db)
        return service.create(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/",
    response_model=AIRecommendationListResponse,
)
def search_recommendations(
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 10,
    application_id: int | None = None,
    recommendation: str | None = None,
    model_version: str | None = None,
    db: Session = Depends(get_db),
):
    service = AIRecommendationService(db)

    return service.search(
        page,
        page_size,
        application_id,
        recommendation,
        model_version,
    )


@router.get(
    "/{recommendation_id}",
    response_model=AIRecommendationResponse,
)
def get_recommendation(
    recommendation_id: int,
    db: Session = Depends(get_db),
):
    try:
        service = AIRecommendationService(db)
        return service.get_by_id(recommendation_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put(
    "/{recommendation_id}",
    response_model=AIRecommendationResponse,
)
def update_recommendation(
    recommendation_id: int,
    request: AIRecommendationUpdate,
    db: Session = Depends(get_db),
):
    try:
        service = AIRecommendationService(db)
        return service.update(
            recommendation_id,
            request,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete(
    "/{recommendation_id}",
)
def delete_recommendation(
    recommendation_id: int,
    db: Session = Depends(get_db),
):
    try:
        service = AIRecommendationService(db)
        service.delete(recommendation_id)

        return {
            "message": "AI recommendation deleted successfully."
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))