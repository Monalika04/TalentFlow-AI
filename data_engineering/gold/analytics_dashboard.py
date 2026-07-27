import pandas as pd


class AnalyticsDashboardBuilder:

    def build(

        self,

        datasets: dict,

    ) -> pd.DataFrame:

        candidates = datasets["candidates"]

        jobs = datasets["jobs"]

        companies = datasets["companies"]

        applications = datasets["applications"]

        recommendations = datasets["recommendations"]

        # ----------------------------
        # Application + Candidate
        # ----------------------------

        df = applications.merge(

            candidates,

            on="candidate_id",

            how="left",

        )

        # ----------------------------
        # + Job
        # ----------------------------

        df = df.merge(

            jobs,

            on="job_id",

            how="left",

        )

        # ----------------------------
        # + Company
        # ----------------------------

        df = df.merge(

            companies,

            on="company_id",

            how="left",

        )

        # ----------------------------
        # + Recommendation
        # ----------------------------

        df = df.merge(

            recommendations,

            on="application_id",

            how="left",

        )

        # ----------------------------
        # Candidate Name
        # ----------------------------

        df["candidate_name"] = (

            df["first_name"]

            + " "

            + df["last_name"]

        )

        # ----------------------------
        # Select Final Columns
        # ----------------------------

        dashboard = df[

            [

                "application_id",

                "candidate_id",

                "candidate_name",

                "city",

                "highest_education",

                "total_experience",

                "current_ctc",

                "expected_ctc",

                "job_id",

                "job_title",

                "department",

                "location",

                "employment_type",

                "company_id",

                "company_name",

                "industry",

                "application_status",

                "application_date",

                "source",

                "ai_match_score",

                "overall_score",

                "skill_score",

                "experience_score",

                "education_score",

                "confidence_score",

                "recommendation",

                "hiring_priority",

            ]

        ]

        return dashboard