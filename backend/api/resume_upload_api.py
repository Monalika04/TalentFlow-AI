from fastapi import (
    APIRouter,
    Depends,
    File,
    UploadFile,
)
from sqlalchemy.orm import Session

from backend.authentication.permissions import require_recruiter
from backend.dependencies.database import get_db
from backend.schemas.resume_schema import ResumeResponse
from backend.services.resume_upload_service import ResumeUploadService

router = APIRouter(
    prefix="/candidates",
    tags=["Resume Upload"],
)


@router.post(
    "/{candidate_id}/resume",
    response_model=ResumeResponse,
    status_code=201,
)
async def upload_resume(
    candidate_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_recruiter=Depends(require_recruiter),
):
    service = ResumeUploadService(db)

    return await service.upload_resume(
        candidate_id,
        file,
    )