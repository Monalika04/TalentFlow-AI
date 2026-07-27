from analytics.queries.analytics_queries import (
    candidate_job_ai_analysis,
)


class DashboardService:

    @staticmethod
    def analytics():

        return candidate_job_ai_analysis()