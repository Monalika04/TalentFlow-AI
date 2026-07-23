from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.authentication.permissions import require_admin
from backend.models.recruiter_model import Recruiter

from backend.dependencies.database import get_db
from backend.schemas.recruiter_schema import (
    RecruiterCreate,
    RecruiterUpdate,
    RecruiterResponse,
    RecruiterListResponse,
)
from backend.services.recruiter_service import RecruiterService

router = APIRouter(
    prefix="/recruiters",
    tags=["Recruiters"],
)


@router.post(
    "/",
    response_model=RecruiterResponse,
)
def create_recruiter(
    request: RecruiterCreate,
    db: Session = Depends(get_db),
    current_recruiter: Recruiter = Depends(require_admin),
):
    service = RecruiterService(db)
    return service.create(request)


@router.get(
    "/{recruiter_id}",
    response_model=RecruiterResponse,
)
def get_recruiter(
    recruiter_id: int,
    db: Session = Depends(get_db),
    current_recruiter: Recruiter = Depends(require_admin),
):
    service = RecruiterService(db)
    return service.get_by_id(recruiter_id)


@router.get(
    "/",
    response_model=RecruiterListResponse,
)
def search_recruiters(
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 10,
    company_id: int | None = None,
    role: str | None = None,
    status: str | None = None,
    db: Session = Depends(get_db),
current_recruiter: Recruiter = Depends(require_admin),
):
    service = RecruiterService(db)

    return service.search(
        page=page,
        page_size=page_size,
        company_id=company_id,
        role=role,
        status=status,
    )


@router.put(
    "/{recruiter_id}",
    response_model=RecruiterResponse,
)
def update_recruiter(
    recruiter_id: int,
    request: RecruiterUpdate,
    db: Session = Depends(get_db),
    current_recruiter: Recruiter = Depends(require_admin),
):
    service = RecruiterService(db)

    return service.update(
        recruiter_id,
        request,
    )


@router.delete(
    "/{recruiter_id}",
)
def delete_recruiter(
    recruiter_id: int,
    db: Session = Depends(get_db),
    current_recruiter: Recruiter = Depends(require_admin),
):
    service = RecruiterService(db)

    service.delete(recruiter_id)

    return {
        "message": "Recruiter deleted successfully."
    }