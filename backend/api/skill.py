from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.dependencies.database import get_db
from backend.schemas.skill_schema import (
    SkillCreate,
    SkillUpdate,
    SkillResponse,
    SkillListResponse,
)
from backend.services.skill_service import SkillService

router = APIRouter(
    prefix="/skills",
    tags=["Skills"],
)


@router.post(
    "/",
    response_model=SkillResponse,
    status_code=201,
)
def create_skill(
    skill: SkillCreate,
    db: Session = Depends(get_db),
):

    return SkillService(db).create_skill(skill)


@router.get(
    "/",
    response_model=SkillListResponse,
)
def search_skills(
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 20,
    category: str | None = None,
    status: str | None = None,
    search: str | None = None,
    db: Session = Depends(get_db),
):

    return SkillService(db).search_skills(
        page,
        page_size,
        category,
        status,
        search,
    )


@router.get(
    "/{skill_id}",
    response_model=SkillResponse,
)
def get_skill(
    skill_id: int,
    db: Session = Depends(get_db),
):

    return SkillService(db).get_skill_by_id(skill_id)


@router.put(
    "/{skill_id}",
    response_model=SkillResponse,
)
def update_skill(
    skill_id: int,
    skill: SkillUpdate,
    db: Session = Depends(get_db),
):

    return SkillService(db).update_skill(
        skill_id,
        skill,
    )


@router.delete(
    "/{skill_id}",
)
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
):

    return SkillService(db).delete_skill(skill_id)