from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.authentication.permissions import require_recruiter
from backend.dependencies.database import get_db
from backend.models.recruiter_model import Recruiter
from backend.schemas.job_schema import (
    JobCreate,
    JobUpdate,
    JobResponse,
    JobListResponse,
)
from backend.services.candidate_ranking_service import (
    CandidateRankingService,
)

from backend.schemas.candidate_ranking_schema import (
    CandidateRankingResponse,
)
from backend.services.job_service import JobService
from backend.services.job_ai_service import JobAIService
from backend.schemas.job_analysis_schema import (
    JobAnalysisResponse,
)

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
    current_recruiter: Recruiter = Depends(require_recruiter),
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
    current_recruiter: Recruiter = Depends(require_recruiter),
):
    return JobService(db).search_jobs(
        page=page,
        page_size=page_size,
        company_id=company_id,
        department=department,
        status=status,
        employment_type=employment_type,
        search=search,
    )


@router.get(
    "/{job_id}",
    response_model=JobResponse,
)
def get_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_recruiter: Recruiter = Depends(require_recruiter),
):
    return JobService(db).get_job_by_id(job_id)

@router.get(
    "/{job_id}/analysis",
    response_model=JobAnalysisResponse,
)
def get_job_analysis(
    job_id: int,
    db: Session = Depends(get_db),
):

    service = JobAIService(db)

    return service.get_job_analysis(
        job_id
    )

@router.get(
    "/{job_id}/ranking",
    response_model=CandidateRankingResponse,
)
def get_candidate_ranking(
    job_id: int,
    db: Session = Depends(get_db),
    current_recruiter: Recruiter = Depends(require_recruiter),
):

    service = CandidateRankingService(db)

    return service.get_job_ranking(
        job_id
    )
    
@router.put(
    "/{job_id}",
    response_model=JobResponse,
)
def update_job(
    job_id: int,
    job: JobUpdate,
    db: Session = Depends(get_db),
    current_recruiter: Recruiter = Depends(require_recruiter),
):
    return JobService(db).update_job(
        job_id=job_id,
        job=job,
    )


@router.delete(
    "/{job_id}",
)
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_recruiter: Recruiter = Depends(require_recruiter),
):
    return JobService(db).delete_job(job_id)