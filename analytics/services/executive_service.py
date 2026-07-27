from analytics.queries.executive_queries import (
    total_candidates,
    total_jobs,
    total_companies,
    total_applications,
    open_jobs,
    closed_jobs,
    active_candidates,
    inactive_candidates,
    average_experience,
    average_current_ctc,
    average_expected_ctc,
    average_ai_match_score,
    applications_by_status,
    jobs_by_department,
    companies_by_industry,
)


class ExecutiveService:

    @staticmethod
    def get_dashboard_metrics():

        return {

            "total_candidates":
                int(total_candidates().iloc[0, 0]),

            "total_jobs":
                int(total_jobs().iloc[0, 0]),

            "total_companies":
                int(total_companies().iloc[0, 0]),

            "total_applications":
                int(total_applications().iloc[0, 0]),

            "open_jobs":
                int(open_jobs().iloc[0, 0]),

            "closed_jobs":
                int(closed_jobs().iloc[0, 0]),

            "active_candidates":
                int(active_candidates().iloc[0, 0]),

            "inactive_candidates":
                int(inactive_candidates().iloc[0, 0]),

            "average_experience":
                float(average_experience().iloc[0, 0]),

            "average_current_ctc":
                float(average_current_ctc().iloc[0, 0]),

            "average_expected_ctc":
                float(average_expected_ctc().iloc[0, 0]),

            "average_ai_match_score":
                float(average_ai_match_score().iloc[0, 0]),

        }

    @staticmethod
    def get_application_status():

        return applications_by_status()

    @staticmethod
    def get_jobs_by_department():

        return jobs_by_department()

    @staticmethod
    def get_companies_by_industry():

        return companies_by_industry()