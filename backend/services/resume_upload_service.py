from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from backend.models.candidate import Candidate
from backend.models.resume import Resume
from backend.repositories.resume_repository import ResumeRepository
from backend.services.file_service import FileService


class ResumeUploadService:

    def __init__(self, db: Session):
        self.db = db
        self.resume_repository = ResumeRepository(db)

    async def upload_resume(
        self,
        candidate_id: int,
        file: UploadFile,
    ):

        # 1. Validate Candidate
        candidate = (
            self.db.query(Candidate)
            .filter(
                Candidate.candidate_id == candidate_id
            )
            .first()
        )

        if candidate is None:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found.",
            )

        # 2. Save File
        uploaded_file = await FileService.save_resume(file)
        latest_version = (
    self.resume_repository.get_latest_version(
        candidate_id
        )
      )

        resume_version = latest_version + 1


        # 4. Create Resume Record
        resume = Resume(
            candidate_id=candidate_id,
            file_name=uploaded_file["file_name"],
            file_path=uploaded_file["file_path"],
            file_type=uploaded_file["file_type"],
            file_size_kb=uploaded_file["file_size_kb"],
            resume_version=resume_version,
            parsing_status="PENDING",
        )

        # 5. Save Metadata
        return self.resume_repository.create(resume)