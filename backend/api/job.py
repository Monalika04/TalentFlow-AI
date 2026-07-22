from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.dependencies.database import get_db
from backend.schemas.job_schema import (
    JobCreate,
    JobUpdate,
    JobResponse,
    JobListResponse,
)
from backend.services.job_service import JobService

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.post(
    "/",
    response_model=JobResponse,
    status_code=201,
)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
):
    return JobService(db).create_job(job)


@router.get(
    "/",
    response_model=JobListResponse,
)
def search_jobs(
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 20,
    company_id: int | None = None,
    department: str | None = None,
    status: str | None = None,
    employment_type: str | None = None,
    search: str | None = None,
    db: Session = Depends(get_db),
):
    return JobService(db).search_jobs(
        page,
        page_size,
        company_id,
        department,
        status,
        employment_type,
        search,
    )


@router.get(
    "/{job_id}",
    response_model=JobResponse,
)
def get_job(
    job_id: int,
    db: Session = Depends(get_db),
):
    return JobService(db).get_job_by_id(job_id)


@router.put(
    "/{job_id}",
    response_model=JobResponse,
)
def update_job(
    job_id: int,
    job: JobUpdate,
    db: Session = Depends(get_db),
):
    return JobService(db).update_job(
        job_id,
        job,
    )


@router.delete(
    "/{job_id}",
)
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
):
    return JobService(db).delete_job(job_id)