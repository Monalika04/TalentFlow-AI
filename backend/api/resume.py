from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.dependencies.database import get_db
from backend.schemas.resume_schema import (
    ResumeCreate,
    ResumeUpdate,
    ResumeResponse,
    ResumeListResponse,
)
from backend.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)


@router.post(
    "/",
    response_model=ResumeResponse,
    status_code=201,
)
def create_resume(
    data: ResumeCreate,
    db: Session = Depends(get_db),
):
    service = ResumeService(db)
    return service.create_resume(data)


@router.get(
    "/",
    response_model=ResumeListResponse,
)
def get_resumes(
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 10,
    candidate_id: int | None = None,
    parsing_status: str | None = None,
    file_type: str | None = None,
    db: Session = Depends(get_db),
):
    service = ResumeService(db)

    return service.search_resumes(
        page=page,
        page_size=page_size,
        candidate_id=candidate_id,
        parsing_status=parsing_status,
        file_type=file_type,
    )


@router.get(
    "/{resume_id}",
    response_model=ResumeResponse,
)
def get_resume(
    resume_id: int,
    db: Session = Depends(get_db),
):
    service = ResumeService(db)
    return service.get_resume_by_id(resume_id)


@router.put(
    "/{resume_id}",
    response_model=ResumeResponse,
)
def update_resume(
    resume_id: int,
    data: ResumeUpdate,
    db: Session = Depends(get_db),
):
    service = ResumeService(db)

    return service.update_resume(
        resume_id,
        data,
    )


@router.delete(
    "/{resume_id}",
)
def delete_resume(
    resume_id: int,
    db: Session = Depends(get_db),
):
    service = ResumeService(db)

    return service.delete_resume(resume_id)