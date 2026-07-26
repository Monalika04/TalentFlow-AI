from typing import Optional

from sqlalchemy.orm import Session

from backend.models.resume_ai_analysis_model import (
    ResumeAIAnalysis,
    AIAnalysisStatus,
)

from backend.models.resume import Resume
class ResumeAIAnalysisRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_analysis(
        self,
        resume_id: int,
        model_name: str,
        prompt_version: str,
        analysis_version: int,
    ) -> ResumeAIAnalysis:

        analysis = ResumeAIAnalysis(
            resume_id=resume_id,
            model_name=model_name,
            prompt_version=prompt_version,
            analysis_version=analysis_version,
            status=AIAnalysisStatus.PENDING,
        )

        self.db.add(analysis)
        self.db.flush()
        self.db.refresh(analysis)

        return analysis

    def get_latest_analysis(
        self,
        resume_id: int,
    ) -> Optional[ResumeAIAnalysis]:

        return (
            self.db.query(ResumeAIAnalysis)
            .filter(
                ResumeAIAnalysis.resume_id == resume_id
            )
            .order_by(
                ResumeAIAnalysis.analysis_version.desc()
            )
            .first()
        )

    def get_analysis_history(
        self,
        resume_id: int,
    ):

        return (
            self.db.query(ResumeAIAnalysis)
            .filter(
                ResumeAIAnalysis.resume_id == resume_id
            )
            .order_by(
                ResumeAIAnalysis.analysis_version.desc()
            )
            .all()
        )

    def update_status(
        self,
        analysis: ResumeAIAnalysis,
        status: AIAnalysisStatus,
    ) -> ResumeAIAnalysis:

        analysis.status = status

        self.db.flush()
        self.db.refresh(analysis)

        return analysis

    def save_raw_text(
        self,
        analysis: ResumeAIAnalysis,
        raw_text: str,
    ) -> ResumeAIAnalysis:

        analysis.raw_resume_text = raw_text

        self.db.flush()
        self.db.refresh(analysis)

        return analysis

    def save_ai_response(
        self,
        analysis: ResumeAIAnalysis,
        response_json: dict,
        execution_time_ms: float | None = None,
        prompt_tokens: int | None = None,
        completion_tokens: int | None = None,
        total_tokens: int | None = None,
    ) -> ResumeAIAnalysis:

        analysis.ai_response_json = response_json
        analysis.execution_time_ms = execution_time_ms
        analysis.prompt_tokens = prompt_tokens
        analysis.completion_tokens = completion_tokens
        analysis.total_tokens = total_tokens

        self.db.flush()
        self.db.refresh(analysis)

        return analysis

    def mark_completed(
        self,
        analysis: ResumeAIAnalysis,
    ) -> ResumeAIAnalysis:

        analysis.status = AIAnalysisStatus.COMPLETED

        self.db.flush()
        self.db.refresh(analysis)

        return analysis

    def mark_failed(
        self,
        analysis: ResumeAIAnalysis,
        error_message: str,
    ) -> ResumeAIAnalysis:

        analysis.status = AIAnalysisStatus.FAILED
        analysis.error_message = error_message

        self.db.flush()
        self.db.refresh(analysis)

        return analysis

    def create_new_version(
        self,
        resume_id: int,
        model_name: str,
        prompt_version: str,
    ) -> ResumeAIAnalysis:

        latest = self.get_latest_analysis(resume_id)

        version = 1

        if latest:
            version = latest.analysis_version + 1

        return self.create_analysis(
            resume_id=resume_id,
            model_name=model_name,
            prompt_version=prompt_version,
            analysis_version=version,
        )
        
    def get_latest_by_resume(
        self,
        resume_id: int,
    ):
        return (
            self.db.query(ResumeAIAnalysis)
            .filter(
                ResumeAIAnalysis.resume_id == resume_id
            )
            .order_by(
                ResumeAIAnalysis.analysis_version.desc()
            )
            .first()
        )
    
    def get_latest_by_candidate(
        self,
        candidate_id: int,
    ):
        return (
            self.db.query(ResumeAIAnalysis)
            .join(
                Resume,
                Resume.resume_id == ResumeAIAnalysis.resume_id,
            )
            .filter(
                Resume.candidate_id == candidate_id,
            )
            .order_by(
                Resume.resume_version.desc(),
                ResumeAIAnalysis.analysis_version.desc(),
            )
            .first()
    )