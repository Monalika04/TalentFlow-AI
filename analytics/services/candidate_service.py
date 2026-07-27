from analytics.queries.candidate_queries import (
    candidates_by_city,
    candidates_by_state,
    candidates_by_country,
    candidates_by_status,
    education_distribution,
    experience_distribution,
    notice_period_distribution,
    salary_distribution,
    top_experienced_candidates,
    candidate_locations,
)


class CandidateService:

    @staticmethod
    def get_candidate_dashboard():

        return {

            "city_distribution":
                candidates_by_city(),

            "state_distribution":
                candidates_by_state(),

            "country_distribution":
                candidates_by_country(),

            "status_distribution":
                candidates_by_status(),

            "education_distribution":
                education_distribution(),

            "experience_distribution":
                experience_distribution(),

            "notice_period_distribution":
                notice_period_distribution(),

            "salary_distribution":
                salary_distribution(),

            "top_candidates":
                top_experienced_candidates(),

            "locations":
                candidate_locations(),
        }