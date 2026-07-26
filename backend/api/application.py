from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.dependencies.database import get_db
from backend.schemas.application_schema import (
    ApplicationCreate,
    ApplicationUpdate,
    ApplicationResponse,
    ApplicationListResponse,
)
from backend.services.application_service import ApplicationService
from backend.services.candidate_matching_service import (
    CandidateMatchingService,
)
router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
)


@router.post(
    "/",
    response_model=ApplicationResponse,
    status_code=201,
)
def create_application(
    data: ApplicationCreate,
    db: Session = Depends(get_db),
):
    service = ApplicationService(db)
    return service.create_application(data)


@router.get(
    "/",
    response_model=ApplicationListResponse,
)
def get_applications(
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 10,
    candidate_id: int | None = None,
    job_id: int | None = None,
    application_status: str | None = None,
    db: Session = Depends(get_db),
):
    service = ApplicationService(db)

    return service.search_applications(
        page=page,
        page_size=page_size,
        candidate_id=candidate_id,
        job_id=job_id,
        application_status=application_status,
    )


@router.get(
    "/{application_id}",
    response_model=ApplicationResponse,
)
def get_application(
    application_id: int,
    db: Session = Depends(get_db),
):
    service = ApplicationService(db)
    return service.get_application_by_id(application_id)
@router.post(
    "/{application_id}/match",
)
def match_candidate(
    application_id: int,
    db: Session = Depends(get_db),
):

    service = CandidateMatchingService(db)

    return service.match_candidate(
        application_id
    )

@router.put(
    "/{application_id}",
    response_model=ApplicationResponse,
)
def update_application(
    application_id: int,
    data: ApplicationUpdate,
    db: Session = Depends(get_db),
):
    service = ApplicationService(db)

    return service.update_application(
        application_id,
        data,
    )


@router.delete(
    "/{application_id}",
)
def delete_application(
    application_id: int,
    db: Session = Depends(get_db),
):
    service = ApplicationService(db)

    return service.delete_application(application_id)