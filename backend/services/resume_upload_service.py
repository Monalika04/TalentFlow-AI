from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from backend.models.resume import Resume
from backend.repositories.candidate_repository import CandidateRepository
from backend.repositories.resume_repository import ResumeRepository
from backend.services.file_service import FileService
from backend.services.resume_ai_service import ResumeAIService


class ResumeUploadService:

    def __init__(self, db: Session):

        self.db = db

        self.candidate_repository = CandidateRepository(db)

        self.resume_repository = ResumeRepository(db)

        self.resume_ai_service = ResumeAIService(db)

    async def upload_resume(
        self,
        candidate_id: int,
        file: UploadFile,
    ):

        # --------------------------------------------------
        # Validate Candidate
        # --------------------------------------------------

        candidate = self.candidate_repository.get_by_id(
            candidate_id
        )

        if candidate is None:

            raise HTTPException(
                status_code=404,
                detail="Candidate not found.",
            )

        # --------------------------------------------------
        # Save Resume File
        # --------------------------------------------------

        uploaded_file = await FileService.save_resume(
            file
        )

        # --------------------------------------------------
        # Resume Version
        # --------------------------------------------------

        latest_version = (
            self.resume_repository.get_latest_version(
                candidate_id
            )
        )

        resume_version = latest_version + 1

        # --------------------------------------------------
        # Create Resume
        # --------------------------------------------------

        resume = Resume(
            candidate_id=candidate_id,
            file_name=uploaded_file["file_name"],
            file_path=uploaded_file["file_path"],
            file_type=uploaded_file["file_type"],
            file_size_kb=uploaded_file["file_size_kb"],
            resume_version=resume_version,
            parsing_status="PENDING",
        )
        
        
        resume = self.resume_repository.create(
            resume
        )

        # SAVE THE RESUME FIRST
        self.db.commit()
        self.db.refresh(resume)

        try:
            
            ai_response = self.resume_ai_service.analyze_resume(
                resume.resume_id
            )

            # Reload resume from database
            resume = self.resume_repository.get_by_id(
                resume.resume_id
            )

            resume.parsing_status = "COMPLETED"

            resume.ai_summary = (
                ai_response.intelligence.professional_summary
            )

            self.resume_repository.update(resume)

            self.db.commit()
            
            



        except Exception as e:

            print("AI ERROR:", e)

            # Reload resume from database
            resume = self.resume_repository.get_by_id(
                resume.resume_id
            )

            resume.parsing_status = "FAILED"

            self.resume_repository.update(resume)

            self.db.commit()

        return resume

            