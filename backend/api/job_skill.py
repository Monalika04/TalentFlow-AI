from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.dependencies.database import get_db
from backend.schemas.job_skill_schema import (
    JobSkillCreate,
    JobSkillUpdate,
    JobSkillResponse,
    JobSkillListResponse,
)
from backend.services.job_skill_service import JobSkillService

router = APIRouter(
    prefix="/job-skills",
    tags=["Job Skills"],
)


@router.post(
    "/",
    response_model=JobSkillResponse,
    status_code=201,
)
def create_job_skill(
    data: JobSkillCreate,
    db: Session = Depends(get_db),
):
    service = JobSkillService(db)
    return service.create_job_skill(data)


@router.get(
    "/",
    response_model=JobSkillListResponse,
)
def get_job_skills(
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 10,
    job_id: int | None = None,
    skill_id: int | None = None,
    is_mandatory: bool | None = None,
    db: Session = Depends(get_db),
):
    service = JobSkillService(db)

    return service.search_job_skills(
        page=page,
        page_size=page_size,
        job_id=job_id,
        skill_id=skill_id,
        is_mandatory=is_mandatory,
    )


@router.get(
    "/{job_skill_id}",
    response_model=JobSkillResponse,
)
def get_job_skill(
    job_skill_id: int,
    db: Session = Depends(get_db),
):
    service = JobSkillService(db)
    return service.get_job_skill_by_id(job_skill_id)


@router.put(
    "/{job_skill_id}",
    response_model=JobSkillResponse,
)
def update_job_skill(
    job_skill_id: int,
    data: JobSkillUpdate,
    db: Session = Depends(get_db),
):
    service = JobSkillService(db)

    return service.update_job_skill(
        job_skill_id,
        data,
    )


@router.delete(
    "/{job_skill_id}",
)
def delete_job_skill(
    job_skill_id: int,
    db: Session = Depends(get_db),
):
    service = JobSkillService(db)

    return service.delete_job_skill(job_skill_id)