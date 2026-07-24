from backend.ai.normalization import normalize_skill_list
from backend.ai.parser_schema import ResumeAIResponse


class ResponseValidator:

    def validate(
        self,
        response: dict,
    ) -> ResumeAIResponse:

        validated = ResumeAIResponse.model_validate(response)

        self._normalize(validated)

        self._validate_business_rules(validated)

        return validated

    def _normalize(
        self,
        response: ResumeAIResponse,
    ) -> None:

        response.facts.technical_skills.programming_languages = (
            normalize_skill_list(
                response.facts.technical_skills.programming_languages
            )
        )

        response.facts.technical_skills.frameworks = (
            normalize_skill_list(
                response.facts.technical_skills.frameworks
            )
        )

        response.facts.technical_skills.databases = (
            normalize_skill_list(
                response.facts.technical_skills.databases
            )
        )

        response.facts.technical_skills.tools = (
            normalize_skill_list(
                response.facts.technical_skills.tools
            )
        )

        response.facts.technical_skills.libraries = (
            normalize_skill_list(
                response.facts.technical_skills.libraries
            )
        )

    def _validate_business_rules(
        self,
        response: ResumeAIResponse,
    ) -> None:

        if response.intelligence.estimated_years_of_experience < 0:
            raise ValueError(
                "Estimated years of experience cannot be negative."
            )

        if not (
            0 <= response.intelligence.ats_score <= 100
        ):
            raise ValueError(
                "ATS score must be between 0 and 100."
            )

        if not (
            0 <= response.intelligence.confidence_score <= 1
        ):
            raise ValueError(
                "Confidence score must be between 0 and 1."
            )