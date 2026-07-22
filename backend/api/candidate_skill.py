from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.dependencies.database import get_db
from backend.schemas.candidate_skill_schema import (
    CandidateSkillCreate,
    CandidateSkillUpdate,
    CandidateSkillResponse,
    CandidateSkillListResponse,
)
from backend.services.candidate_skill_service import CandidateSkillService

router = APIRouter(
    prefix="/candidate-skills",
    tags=["Candidate Skills"],
)


@router.post(
    "/",
    response_model=CandidateSkillResponse,
    status_code=201,
)
def create_candidate_skill(
    candidate_skill: CandidateSkillCreate,
    db: Session = Depends(get_db),
):
    return CandidateSkillService(db).create_candidate_skill(
        candidate_skill
    )


@router.get(
    "/",
    response_model=CandidateSkillListResponse,
)
def search_candidate_skills(
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 20,
    candidate_id: int | None = None,
    skill_id: int | None = None,
    proficiency_level: str | None = None,
    db: Session = Depends(get_db),
):
    return CandidateSkillService(db).search_candidate_skills(
        page,
        page_size,
        candidate_id,
        skill_id,
        proficiency_level,
    )


@router.get(
    "/{candidate_skill_id}",
    response_model=CandidateSkillResponse,
)
def get_candidate_skill(
    candidate_skill_id: int,
    db: Session = Depends(get_db),
):
    return CandidateSkillService(db).get_candidate_skill_by_id(
        candidate_skill_id
    )


@router.put(
    "/{candidate_skill_id}",
    response_model=CandidateSkillResponse,
)
def update_candidate_skill(
    candidate_skill_id: int,
    candidate_skill: CandidateSkillUpdate,
    db: Session = Depends(get_db),
):
    return CandidateSkillService(db).update_candidate_skill(
        candidate_skill_id,
        candidate_skill,
    )


@router.delete(
    "/{candidate_skill_id}",
)
def delete_candidate_skill(
    candidate_skill_id: int,
    db: Session = Depends(get_db),
):
    return CandidateSkillService(db).delete_candidate_skill(
        candidate_skill_id
    )