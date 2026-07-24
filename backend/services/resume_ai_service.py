import time
import os
import json
from dotenv import load_dotenv

load_dotenv()

from sqlalchemy.orm import Session

from backend.ai.ai_client import GeminiClient
from backend.ai.ai_mapper import AIMapper
from backend.ai.parser_schema import ResumeAIResponse
from backend.ai.prompt_builder import PromptBuilder
from backend.ai.response_validator import ResponseValidator
from backend.ai.resume_parser import ResumeParser

from backend.models.candidate_skill import CandidateSkill
from backend.models.resume_ai_analysis_model import AIAnalysisStatus
from backend.models.skill import Skill

from backend.repositories.candidate_repository import CandidateRepository
from backend.repositories.candidate_skill_repository import (
    CandidateSkillRepository,
)
from backend.repositories.certification_repository import (
    CertificationRepository,
)
from backend.repositories.education_repository import (
    EducationRepository,
)
from backend.repositories.experience_repository import (
    ExperienceRepository,
)
from backend.repositories.language_repository import (
    LanguageRepository,
)
from backend.repositories.project_repository import (
    ProjectRepository,
)
from backend.repositories.resume_ai_analysis_repository import (
    ResumeAIAnalysisRepository,
)
from backend.repositories.resume_repository import ResumeRepository
from backend.repositories.skill_repository import SkillRepository


class ResumeAIService:

    MODEL_NAME = "gemini-3.6-flash"
    PROMPT_VERSION = "v1.0"

    def __init__(self, db: Session):

        self.db = db

        # Repositories
        self.resume_repository = ResumeRepository(db)
        self.analysis_repository = ResumeAIAnalysisRepository(db)
        self.candidate_repository = CandidateRepository(db)
        self.skill_repository = SkillRepository(db)
        self.candidate_skill_repository = CandidateSkillRepository(db)
        self.experience_repository = ExperienceRepository(db)
        self.education_repository = EducationRepository(db)
        self.project_repository = ProjectRepository(db)
        self.certification_repository = CertificationRepository(db)
        self.language_repository = LanguageRepository(db)

        # AI Components
        self.resume_parser = ResumeParser()
        self.prompt_builder = PromptBuilder()
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not found in .env")

        self.gemini_client = GeminiClient(api_key=api_key)
        self.response_validator = ResponseValidator()

    def analyze_resume(
        self,
        resume_id: int,
    ) -> ResumeAIResponse:

        analysis = None

        try:

            resume = self._load_resume(resume_id)

            analysis = (
                self.analysis_repository.create_new_version(
                    resume_id=resume.resume_id,
                    model_name=self.MODEL_NAME,
                    prompt_version=self.PROMPT_VERSION,
                )
            )

            self._mark_status(
                analysis,
                AIAnalysisStatus.PROCESSING,
            )

            resume_text = self._extract_resume_text(resume)

            start_time = time.perf_counter()

            ai_response = self._generate_ai_analysis(resume_text)

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

            self.db.commit()

            return ai_response
        except Exception as ex:

            print("\n" + "=" * 80)
            print("AI ANALYSIS FAILED")
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

        return self.response_validator.validate(
            raw_json
        )
    
    
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
            response_json=ai_response.model_dump(mode="json"),
            execution_time_ms=execution_time_ms,
        )


    def _mark_status(
        self,
        analysis,
        status: AIAnalysisStatus,
    ):

        self.analysis_repository.update_status(
            analysis,
            status,
        )

    def _update_candidate_data(
        self,
        resume,
        ai_response: ResumeAIResponse,
    ):

        candidate = self.candidate_repository.get_by_id(
            resume.candidate_id
        )

        if candidate is None:
            raise ValueError(
                f"Candidate {resume.candidate_id} not found."
            )

        self._update_candidate_profile(
            candidate,
            ai_response,
        )

        self._sync_skills(
            candidate.candidate_id,
            ai_response,
        )

        self._sync_experience(
            candidate.candidate_id,
            ai_response,
        )

        self._sync_education(
            candidate.candidate_id,
            ai_response,
        )

        self._sync_projects(
            candidate.candidate_id,
            ai_response,
        )

        self._sync_certifications(
            candidate.candidate_id,
            ai_response,
        )

        self._sync_languages(
            candidate.candidate_id,
            ai_response,
        )

    def _update_candidate_profile(
        self,
        candidate,
        ai_response: ResumeAIResponse,
    ):

        candidate = AIMapper.update_candidate(
            candidate=candidate,
            personal=ai_response.facts.personal_information,
            estimated_experience=(
                ai_response.intelligence.estimated_years_of_experience
            ),
        )

        self.candidate_repository.update(
            candidate
        )
    def _sync_skills(
        self,
        candidate_id: int,
        ai_response: ResumeAIResponse,
    ):

        # Delete old candidate skills
        self.candidate_skill_repository.delete_by_candidate(
            candidate_id
        )

        technical = ai_response.facts.technical_skills

        # Store each skill with its category
        categorized_skills = []

        for skill in technical.programming_languages:
            categorized_skills.append(
                (skill, "PROGRAMMING_LANGUAGE")
            )

        for skill in technical.frameworks:
            categorized_skills.append(
                (skill, "FRAMEWORK")
            )

        for skill in technical.databases:
            categorized_skills.append(
                (skill, "DATABASE")
            )

        for skill in technical.cloud:
            categorized_skills.append(
                (skill, "CLOUD")
            )

        for skill in technical.tools:
            categorized_skills.append(
                (skill, "TOOL")
            )

        for skill in technical.libraries:
            categorized_skills.append(
                (skill, "LIBRARY")
            )

        # Remove duplicate skills
        unique_skills = {}

        for skill_name, category in categorized_skills:
            if skill_name not in unique_skills:
                unique_skills[skill_name] = category

        # Save skills
        for skill_name, category in unique_skills.items():

            skill = self.skill_repository.get_by_name(
                skill_name
            )

            if skill is None:

                skill = Skill(
                    skill_name=skill_name,
                    category=category,
                    description=None,
                    status="ACTIVE",
                )

                skill = self.skill_repository.create(
                    skill
                )

            candidate_skill = CandidateSkill(
                candidate_id=candidate_id,
                skill_id=skill.skill_id,
                proficiency_level=None,
                years_experience=None,
                last_used=None,
                is_primary=False,
            )

            self.candidate_skill_repository.create(
                candidate_skill
            )



    def _sync_experience(
        self,
        candidate_id: int,
        ai_response: ResumeAIResponse,
    ):

        self.experience_repository.delete_by_candidate(
            candidate_id
        )

        for experience in ai_response.facts.experience:

            model = AIMapper.to_experience(
                candidate_id,
                experience,
            )

            self.experience_repository.create(
                model
            )

    def _sync_education(
        self,
        candidate_id: int,
        ai_response: ResumeAIResponse,
    ):

        self.education_repository.delete_by_candidate(
            candidate_id
        )

        for education in ai_response.facts.education:

            model = AIMapper.to_education(
                candidate_id,
                education,
            )

            self.education_repository.create(
                model
            )

    def _sync_projects(
        self,
        candidate_id: int,
        ai_response: ResumeAIResponse,
    ):

        self.project_repository.delete_by_candidate(
            candidate_id
        )

        for project in ai_response.facts.projects:

            model = AIMapper.to_project(
                candidate_id,
                project,
            )

            self.project_repository.create(
                model
            )

    def _sync_certifications(
        self,
        candidate_id: int,
        ai_response: ResumeAIResponse,
    ):

        self.certification_repository.delete_by_candidate(
            candidate_id
        )

        for certification in ai_response.facts.certifications:

            model = AIMapper.to_certification(
                candidate_id,
                certification,
            )

            self.certification_repository.create(
                model
            )

    def _sync_languages(
        self,
        candidate_id: int,
        ai_response: ResumeAIResponse,
    ):

        self.language_repository.delete_by_candidate(
            candidate_id
        )

        for language in ai_response.facts.languages:

            model = AIMapper.to_language(
                candidate_id,
                language,
            )

            self.language_repository.create(
                model
            )