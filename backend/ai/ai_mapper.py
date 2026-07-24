from datetime import date, datetime
from typing import Optional

from backend.ai.parser_schema import (
    Certification as AICertification,
    Education as AIEducation,
    Experience as AIExperience,
    Language as AILanguage,
    PersonalInformation,
    Project as AIProject,
)

from backend.models.candidate import Candidate
from backend.models.certification import Certification
from backend.models.education import Education
from backend.models.experience import Experience
from backend.models.language import Language
from backend.models.project import Project


class AIMapper:

    @staticmethod
    def _parse_date(value: str | None) -> Optional[date]:
        if not value:
            return None

        value = value.strip()

        formats = (
            "%Y-%m-%d",
            "%Y/%m/%d",
            "%d-%m-%Y",
            "%d/%m/%Y",
            "%b %Y",
            "%B %Y",
            "%Y",
        )

        for fmt in formats:
            try:
                return datetime.strptime(value, fmt).date()
            except ValueError:
                continue

        return None

    @staticmethod
    def update_candidate(
        candidate: Candidate,
        personal: PersonalInformation,
        estimated_experience: float,
    ) -> Candidate:

        if personal.full_name:
            names = personal.full_name.strip().split()

            candidate.first_name = names[0]
            candidate.last_name = (
                " ".join(names[1:])
                if len(names) > 1
                else ""
            )

        if personal.email:
            candidate.email = str(personal.email)

        candidate.phone = personal.phone

        if personal.linkedin:
            candidate.linkedin_url = str(personal.linkedin)

        if personal.github:
            candidate.github_url = str(personal.github)

        if personal.portfolio:
            candidate.portfolio_url = str(personal.portfolio)

        candidate.total_experience = estimated_experience

        if personal.location:
            candidate.city = personal.location

        return candidate

    @staticmethod
    def to_experience(
        candidate_id: int,
        experience: AIExperience,
    ) -> Experience:

        start_date = AIMapper._parse_date(
            experience.start_date
        )

        end_date = AIMapper._parse_date(
            experience.end_date
        )

        return Experience(
            candidate_id=candidate_id,
            company_name=experience.company,
            job_title=experience.designation,

            # Required DB field
            start_date=start_date or date(1900, 1, 1),

            end_date=end_date,

            currently_working=end_date is None,

            description="\n".join(
                experience.responsibilities
            ),

            # Optional fields
            employment_type=None,
            location=None,
        )

    @staticmethod
    def to_education(
        candidate_id: int,
        education: AIEducation,
    ) -> Education:

        value = (
            education.percentage
            if education.percentage is not None
            else education.cgpa
        )

        return Education(
            candidate_id=candidate_id,
            degree=education.degree,
            field_of_study=education.specialization,
            institution_name=education.institution,
            grade_or_percentage=value,
            end_year=education.passing_year,
        )

    @staticmethod
    def to_project(
        candidate_id: int,
        project: AIProject,
    ) -> Project:

        return Project(
            candidate_id=candidate_id,
            project_name=project.title,
            description=project.description,
            technologies=", ".join(
                project.technologies
            ),
            github_url=(
                str(project.github_url)
                if project.github_url
                else None
            ),
            live_url=(
                str(project.live_url)
                if project.live_url
                else None
            ),
        )

    @staticmethod
    def to_certification(
        candidate_id: int,
        certification: AICertification,
    ) -> Certification:

        return Certification(
            candidate_id=candidate_id,
            certification_name=certification.name,
            issuing_organization=certification.issuer,
        )

    @staticmethod
    def to_language(
        candidate_id: int,
        language: AILanguage,
    ) -> Language:

        return Language(
            candidate_id=candidate_id,
            language_name=language.name,
            proficiency=language.proficiency,
        )