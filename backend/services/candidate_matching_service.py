from decimal import Decimal

from fastapi import HTTPException

from backend.repositories.application_repository import (
    ApplicationRepository,
)
from backend.repositories.ai_recommendation_repository import (
    AIRecommendationRepository,
)
from backend.repositories.resume_ai_analysis_repository import (
    ResumeAIAnalysisRepository,
)
from backend.repositories.job_ai_analysis_repository import (
    JobAIAnalysisRepository,
)
from backend.models.ai_recommendation import AIRecommendation

class CandidateMatchingService:

    MODEL_VERSION = "v1.0"

    def __init__(self, db):

        self.db = db

        self.application_repository = (
            ApplicationRepository(db)
        )

        self.resume_analysis_repository = (
            ResumeAIAnalysisRepository(db)
        )

        self.job_analysis_repository = (
            JobAIAnalysisRepository(db)
        )

        self.ai_repository = (
            AIRecommendationRepository(db)
        )

    def match_candidate(
        self,
        application_id: int,
    ):

        # ---------------------------------------
        # Load Application
        # ---------------------------------------

        application = (
            self.application_repository.get_by_id(
                application_id
            )
        )

        if application is None:

            raise HTTPException(
                status_code=404,
                detail="Application not found.",
            )

        # ---------------------------------------
        # Load Resume AI Analysis
        # ---------------------------------------

        resume_analysis = (
            self.resume_analysis_repository.get_latest_by_candidate(
                application.candidate_id
            )
        )

        if resume_analysis is None:

            raise HTTPException(
                status_code=404,
                detail="Resume AI analysis not found.",
            )

        # ---------------------------------------
        # Load Job AI Analysis
        # ---------------------------------------

        job_analysis = (
            self.job_analysis_repository.get_latest_by_job(
                application.job_id
            )
        )

        if job_analysis is None:

            raise HTTPException(
                status_code=404,
                detail="Job AI analysis not found.",
            )

        # ---------------------------------------
        # Debug
        # ---------------------------------------

        print("Application Loaded")
        print("Resume Analysis Loaded")
        print("Job Analysis Loaded")

        print(resume_analysis.ai_response_json.keys())
        print(job_analysis.ai_response_json.keys())

        # ---------------------------------------
        # Skill Matching
        # ---------------------------------------

        skill_result = self._calculate_skill_score(
            resume_analysis,
            job_analysis,
        )

        print(skill_result)

        # ---------------------------------------
        # Step 9: Calculate All Scores
        # ---------------------------------------

        experience_score = (
            self._calculate_experience_score(
                resume_analysis,
                job_analysis,
            )
        )

        education_score = (
            self._calculate_education_score(
                resume_analysis,
                job_analysis,
            )
        )

        confidence_score = (
            self._calculate_confidence_score(
                resume_analysis,
            )
        )

        overall_score = (
            self._calculate_overall_score(
                skill_result["skill_score"],
                experience_score,
                education_score,
                confidence_score,
            )
        )

        recommendation = (
            self._recommendation(
                overall_score,
            )
        )

        reasoning = (
            self._reasoning(
                overall_score,
                skill_result["missing_skills"],
            )
        )

        print(overall_score)
        print(recommendation)
        # ---------------------------------------
# Save AI Recommendation
# ---------------------------------------

        recommendation_record = AIRecommendation(

            application_id=application.application_id,

            overall_score=Decimal(str(overall_score)),

            skill_score=Decimal(
                str(skill_result["skill_score"])
            ),

            experience_score=Decimal(
                str(experience_score)
            ),

            education_score=Decimal(
                str(education_score)
            ),

            confidence_score=Decimal(
                str(confidence_score)
            ),

            missing_skills=", ".join(
                skill_result["missing_skills"]
            ),

            strengths=", ".join(
                skill_result["matched_skills"]
            ),

            recommendation=recommendation,

            reasoning=reasoning,

            model_version=self.MODEL_VERSION,
        )

        self.ai_repository.create(
            recommendation_record
        )

        # ---------------------------------------
        # Update Application Score
        # ---------------------------------------

        application.ai_match_score = Decimal(
            str(overall_score)
        )

        self.application_repository.update()

        return {
            "skill_result": skill_result,
            "experience_score": experience_score,
            "education_score": education_score,
            "confidence_score": confidence_score,
            "overall_score": overall_score,
            "recommendation": recommendation,
            "reasoning": reasoning,
        }

    def _calculate_skill_score(
        self,
        resume_analysis,
        job_analysis,
    ):

        candidate_skills = set()

        technical = (
            resume_analysis.ai_response_json["facts"][
                "technical_skills"
            ]
        )

        # Collect candidate skills
        for category in technical.values():

            if isinstance(category, list):

                for skill in category:

                    candidate_skills.add(
                        skill.lower().strip()
                    )

        requirements = (
            job_analysis.ai_response_json[
                "requirements"
            ]
        )

        mandatory_skills = {
            skill.lower().strip()
            for skill in requirements[
                "mandatory_skills"
            ]
        }

        preferred_skills = {
            skill.lower().strip()
            for skill in requirements[
                "preferred_skills"
            ]
        }

        matched_mandatory = (
            candidate_skills &
            mandatory_skills
        )

        matched_preferred = (
            candidate_skills &
            preferred_skills
        )

        missing_skills = (
            mandatory_skills -
            candidate_skills
        )

        mandatory_score = 100

        if mandatory_skills:

            mandatory_score = (
                len(matched_mandatory)
                / len(mandatory_skills)
            ) * 100

        preferred_score = 100

        if preferred_skills:

            preferred_score = (
                len(matched_preferred)
                / len(preferred_skills)
            ) * 100

        skill_score = (
            mandatory_score * 0.80
            +
            preferred_score * 0.20
        )

        return {
            "skill_score": round(skill_score, 2),
            "matched_skills": sorted(
                matched_mandatory |
                matched_preferred
            ),
            "missing_skills": sorted(
                missing_skills
            ),
        }
        
    
    def _calculate_experience_score(
        self,
        resume_analysis,
        job_analysis,
    ):

        candidate_exp = (
            resume_analysis.ai_response_json[
                "intelligence"
            ][
                "estimated_years_of_experience"
            ]
        )

        minimum_exp = (
            job_analysis.ai_response_json[
                "requirements"
            ][
                "minimum_experience"
            ]
        )

        if minimum_exp is None:
            return 100

        if candidate_exp >= minimum_exp:
            return 100

        score = (
            candidate_exp /
            minimum_exp
        ) * 100

        return round(score, 2)
    
    
    def _calculate_education_score(
        self,
        resume_analysis,
        job_analysis,
    ):

        candidate = (
            resume_analysis.ai_response_json[
                "facts"
            ][
                "education"
            ]
        )

        required = (
            job_analysis.ai_response_json[
                "requirements"
            ][
                "education"
            ]
        )

        if not required:
            return 100

        if not candidate:
            return 0

        candidate_degree = (
            candidate[0]["degree"]
            .lower()
        )

        for degree in required:

            if degree.lower() in candidate_degree:
                return 100

        return 50
    
    def _calculate_confidence_score(
        self,
        resume_analysis,
    ):

        confidence = (
            resume_analysis.ai_response_json[
                "intelligence"
            ][
                "confidence_score"
            ]
        )

        return round(
            confidence * 100,
            2,
        )
        
    def _calculate_overall_score(
        self,
        skill_score,
        experience_score,
        education_score,
        confidence_score,
    ):

        overall = (

            skill_score * 0.40

            +

            experience_score * 0.20

            +

            education_score * 0.10

            +

            confidence_score * 0.30

        )

        return round(
            overall,
            2,
        )
        
    def _recommendation(
        self,
        overall,
    ):

        if overall >= 90:
            return "STRONGLY_RECOMMENDED"

        if overall >= 75:
            return "RECOMMENDED"

        if overall >= 60:
            return "CONSIDER"

        return "NOT_RECOMMENDED"
    
    def _reasoning(
        self,
        overall,
        missing_skills,
    ):

        if overall >= 90:

            return (
                "Excellent candidate. "
                "Highly aligned with job requirements."
            )

        if overall >= 75:

            return (
                "Good candidate with minor skill gaps."
            )

        if overall >= 60:

            return (
                "Candidate partially matches the role."
            )

        return (
            "Candidate does not sufficiently match the required profile."
        )