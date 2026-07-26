import os
import time

from dotenv import load_dotenv
from fastapi import HTTPException
from backend.ai.ai_client import GeminiClient
from backend.ai.parser_schema import JobAIResponse
from backend.ai.prompt_builder import PromptBuilder
from backend.ai.response_validator import ResponseValidator
from backend.models.job import Job
from backend.models.job_ai_analysis_model import (
    JobAIAnalysisStatus,
)
from backend.repositories.job_ai_analysis_repository import (
    JobAIAnalysisRepository,
)
from backend.repositories.job_repository import JobRepository
from backend.repositories.job_skill_repository import (
    JobSkillRepository,
)
from backend.repositories.skill_repository import SkillRepository
from backend.models.job_skill import JobSkill


load_dotenv()


class JobAIService:

    MODEL_NAME = "gemini-3.6-flash"

    PROMPT_VERSION = "v1.0"

    def __init__(self, db):

        self.db = db

        self.job_repository = JobRepository(db)

        self.analysis_repository = (
            JobAIAnalysisRepository(db)
        )

        self.skill_repository = SkillRepository(db)

        self.job_skill_repository = (
            JobSkillRepository(db)
        )

        self.prompt_builder = PromptBuilder()

        self.response_validator = (
            ResponseValidator()
        )

        self.gemini_client = GeminiClient(
            os.getenv("GEMINI_API_KEY")
        )
    def analyze_job(
        self,
        job_id: int,
    ) -> JobAIResponse:

        analysis = None

        try:

            print("STEP 1 - Load Job")
            job = self._load_job(job_id)

            print("STEP 2 - Create Analysis")
            analysis = self.analysis_repository.create_new_version(
                job_id=job.job_id,
                model_name=self.MODEL_NAME,
                prompt_version=self.PROMPT_VERSION,
            )

            print("STEP 3 - Mark Processing")
            self._mark_status(
                analysis,
                JobAIAnalysisStatus.PROCESSING,
            )

            print("STEP 4 - Generate AI")
            start_time = time.perf_counter()

            ai_response = self._generate_ai_analysis(job)

            print("STEP 5 - AI Generated")

            execution_time = (
                time.perf_counter() - start_time
            ) * 1000

            print("STEP 6 - Persist Analysis")
            self._persist_analysis(
                analysis=analysis,
                job=job,
                ai_response=ai_response,
                execution_time_ms=execution_time,
            )

            print("STEP 7 - Sync Skills")
            self._sync_job_skills(
                job,
                ai_response,
            )

            print("STEP 8 - Mark Completed")
            self._mark_status(
                analysis,
                JobAIAnalysisStatus.COMPLETED,
            )

            print("STEP 9 - Commit")
            self.db.commit()

            print("STEP 10 - Success")

            return ai_response

        except Exception as ex:

            print("\n" + "=" * 80)
            print("JOB AI FAILED")
            print(type(ex).__name__)
            print(str(ex))
            print("=" * 80 + "\n")

            self.db.rollback()

            if analysis:
                self.analysis_repository.mark_failed(
                    analysis,
                    str(ex),
                )
                self.db.commit()

            raise


    def _load_job(
        self,
        job_id: int,
    ) -> Job:

        job = self.job_repository.get_by_id(
            job_id
        )

        if job is None:

            raise ValueError(
                "Job not found."
            )

        return job

    def _mark_status(
        self,
        analysis,
        status,
    ):

        self.analysis_repository.update_status(
            analysis,
            status,
        )

    def _generate_ai_analysis(
        self,
        job: Job,
    ) -> JobAIResponse:

        prompt = self.prompt_builder.build_job_prompt(
            job.job_description
        )

        raw_json = self.gemini_client.generate(
            prompt
        )

        return self.response_validator.validate(
            raw_json,
            JobAIResponse,
        )

    def _persist_analysis(
        self,
        analysis,
        job: Job,
        ai_response: JobAIResponse,
        execution_time_ms: float,
    ):

        self.analysis_repository.save_raw_text(
            analysis,
            job.job_description,
        )

        self.analysis_repository.save_ai_response(
            analysis=analysis,
            response_json=ai_response.model_dump(
                mode="json"
            ),
            execution_time_ms=execution_time_ms,
        )

    def _sync_job_skills(
        self,
        job: Job,
        ai_response: JobAIResponse,
    ):

        requirements = ai_response.requirements

        # -----------------------------
        # Mandatory Skills
        # -----------------------------

        for skill_name in requirements.mandatory_skills:

            skill = self.skill_repository.get_or_create(
                skill_name=skill_name,
                category="GENERAL",
            )

            existing = (
                self.job_skill_repository.get_by_job_and_skill(
                    job.job_id,
                    skill.skill_id,
                )
            )

            if existing:
                continue

            self.job_skill_repository.create(

                JobSkill(
                    job_id=job.job_id,
                    skill_id=skill.skill_id,
                    importance_weight=5,
                    is_mandatory=True,
                )

            )

        # -----------------------------
        # Preferred Skills
        # -----------------------------

        for skill_name in requirements.preferred_skills:

            skill = self.skill_repository.get_or_create(
                skill_name=skill_name,
                category="GENERAL",
            )

            existing = (
                self.job_skill_repository.get_by_job_and_skill(
                    job.job_id,
                    skill.skill_id,
                )
            )

            if existing:
                continue

            self.job_skill_repository.create(

                JobSkill(
                    job_id=job.job_id,
                    skill_id=skill.skill_id,
                    importance_weight=3,
                    is_mandatory=False,
                )

            )
    def get_job_analysis(
        self,
        job_id: int,
    ):

        analysis = (
            self.analysis_repository.get_latest_by_job_id(
                job_id
            )
        )

        if analysis is None:

            raise HTTPException(
                status_code=404,
                detail="Job AI analysis not found.",
            )

        return analysis