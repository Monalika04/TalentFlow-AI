from analytics.queries.job_queries import (
    jobs_by_department,
    jobs_by_company,
    jobs_by_location,
    jobs_by_employment_type,
    open_vs_closed_jobs,
    vacancies_by_department,
    average_salary_by_department,
    experience_required,
    top_paying_jobs,
    job_summary,
)


class JobService:

    @staticmethod
    def get_job_dashboard():

        return {

            "department_distribution":
                jobs_by_department(),

            "company_distribution":
                jobs_by_company(),

            "location_distribution":
                jobs_by_location(),

            "employment_distribution":
                jobs_by_employment_type(),

            "job_status":
                open_vs_closed_jobs(),

            "vacancies":
                vacancies_by_department(),

            "salary":
                average_salary_by_department(),

            "experience":
                experience_required(),

            "top_paying":
                top_paying_jobs(),

            "summary":
                job_summary(),
        }