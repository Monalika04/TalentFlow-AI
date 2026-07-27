from analytics.queries.application_queries import (
    applications_by_status,
    applications_by_source,
    applications_by_month,
    applications_by_candidate,
    applications_by_job,
    ai_match_distribution,
    recruiter_notes,
    application_summary,
    average_match_score,
    highest_match_candidates,
)


class ApplicationService:

    @staticmethod
    def get_application_dashboard():

        return {

            "status":
                applications_by_status(),

            "source":
                applications_by_source(),

            "monthly":
                applications_by_month(),

            "candidate":
                applications_by_candidate(),

            "job":
                applications_by_job(),

            "match_distribution":
                ai_match_distribution(),

            "notes":
                recruiter_notes(),

            "summary":
                application_summary(),

            "average_score":
                average_match_score(),

            "top_matches":
                highest_match_candidates(),
        }