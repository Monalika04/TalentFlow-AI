import time
from sqlalchemy.orm import Session

from backend.ai.ai_client import GeminiClient
from backend.ai.prompt_builder import PromptBuilder
from backend.ai.response_validator import ResponseValidator
from backend.ai.resume_parser import ResumeParser

from backend.ai.parser_schema import ResumeAIResponse

from backend.models.resume_ai_analysis_model import AIAnalysisStatus

from backend.repositories.resume_repository import ResumeRepository
from backend.repositories.resume_ai_analysis_repository import (
    ResumeAIAnalysisRepository,
)


class ResumeAIService:

    MODEL_NAME = "gemini-2.5-flash"
    PROMPT_VERSION = "v1.0"

    def __init__(self, db: Session):

        self.db = db

        self.resume_repository = ResumeRepository(db)
        self.analysis_repository = ResumeAIAnalysisRepository(db)

        self.resume_parser = ResumeParser()
        self.prompt_builder = PromptBuilder()
        self.gemini_client = GeminiClient()
        self.response_validator = ResponseValidator()

    def analyze_resume(
        self,
        resume_id: int,
    ) -> ResumeAIResponse:

        analysis = None

        try:

            resume = self._load_resume(resume_id)

            analysis = self.analysis_repository.create_new_version(
                resume_id=resume.resume_id,
                model_name=self.MODEL_NAME,
                prompt_version=self.PROMPT_VERSION,
            )

            self._mark_status(
                analysis,
                AIAnalysisStatus.PROCESSING,
            )

            resume_text = self._extract_resume_text(resume)

            start_time = time.perf_counter()

            ai_response = self._generate_ai_analysis(
                resume_text
            )

            execution_time = (
                time.perf_counter() - start_time
            ) * 1000

            self._persist_analysis(
                analysis=analysis,
                raw_resume_text=resume_text,
                ai_response=ai_response,
                execution_time_ms=execution_time,
            )

            self._update_candidate_data(
                resume,
                ai_response,
            )

            self._mark_status(
                analysis,
                AIAnalysisStatus.COMPLETED,
            )

            return ai_response

        except Exception as ex:

            if analysis is not None:

                self.analysis_repository.mark_failed(
                    analysis,
                    str(ex),
                )

            raise

    def _load_resume(
        self,
        resume_id: int,
    ):

        resume = self.resume_repository.get_by_id(
            resume_id
        )

        if resume is None:

            raise ValueError(
                f"Resume {resume_id} not found."
            )

        return resume

    def _extract_resume_text(
        self,
        resume,
    ) -> str:

        return self.resume_parser.extract_text(
            resume.file_path
        )

    def _generate_ai_analysis(
        self,
        resume_text: str,
    ) -> ResumeAIResponse:

        prompt = self.prompt_builder.build_prompt(
            resume_text
        )

        raw_json = self.gemini_client.generate(
            prompt
        )

        validated = self.response_validator.validate(
            raw_json
        )

        return validated

    def _persist_analysis(
        self,
        analysis,
        raw_resume_text: str,
        ai_response: ResumeAIResponse,
        execution_time_ms: float,
    ):

        self.analysis_repository.save_raw_text(
            analysis,
            raw_resume_text,
        )

        self.analysis_repository.save_ai_response(
            analysis=analysis,
            response_json=ai_response.model_dump(),
            execution_time_ms=execution_time_ms,
        )

    def _update_candidate_data(
        self,
        resume,
        ai_response: ResumeAIResponse,
    ):

        """
        Update normalized tables.

        Candidate
        Skills
        Experience
        Education
        Projects

        This method should call your existing repositories.
        """

        pass

    def _mark_status(
        self,
        analysis,
        status: AIAnalysisStatus,
    ):

        self.analysis_repository.update_status(
            analysis,
            status,
        )