from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.dependencies.database import get_db
from backend.schemas.candidate_schema import (
    CandidateCreate,
    CandidateUpdate,
    CandidateListResponse,
    CandidateResponse,
)
from backend.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"],
)


@router.post(
    "/",
    response_model=CandidateResponse,
    status_code=201,
)
def create_candidate(
    candidate: CandidateCreate,
    db: Session = Depends(get_db),
):

    return CandidateService(db).create_candidate(candidate)


@router.get(
    "/",
    response_model=CandidateListResponse,
)
def search_candidates(
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 20,
    city: str | None = None,
    status: str | None = None,
    search: str | None = None,
    db: Session = Depends(get_db),
):

    return CandidateService(db).search_candidates(
        page,
        page_size,
        city,
        status,
        search,
    )


@router.get(
    "/{candidate_id}",
    response_model=CandidateResponse,
)
def get_candidate(
    candidate_id: int,
    db: Session = Depends(get_db),
):

    return CandidateService(db).get_candidate_by_id(
        candidate_id
    )


@router.put(
    "/{candidate_id}",
    response_model=CandidateResponse,
)
def update_candidate(
    candidate_id: int,
    candidate: CandidateUpdate,
    db: Session = Depends(get_db),
):

    return CandidateService(db).update_candidate(
        candidate_id,
        candidate,
    )


@router.delete(
    "/{candidate_id}",
)
def delete_candidate(
    candidate_id: int,
    db: Session = Depends(get_db),
):

    return CandidateService(db).delete_candidate(
        candidate_id
    )