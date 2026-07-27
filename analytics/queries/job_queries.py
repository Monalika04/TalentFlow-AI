from analytics.database import db


def jobs_by_department():

    query = f"""
    SELECT

        department,

        COUNT(*) AS total_jobs

    FROM
        {db.gold_table("jobs")}

    GROUP BY
        department

    ORDER BY
        total_jobs DESC
    """

    return db.dataframe(query)


def jobs_by_company():

    query = f"""
    SELECT

        company_id,

        COUNT(*) AS total_jobs

    FROM
        {db.gold_table("jobs")}

    GROUP BY
        company_id

    ORDER BY
        total_jobs DESC
    """

    return db.dataframe(query)


def jobs_by_location():

    query = f"""
    SELECT

        location,

        COUNT(*) AS total_jobs

    FROM
        {db.gold_table("jobs")}

    GROUP BY
        location

    ORDER BY
        total_jobs DESC
    """

    return db.dataframe(query)


def jobs_by_employment_type():

    query = f"""
    SELECT

        employment_type,

        COUNT(*) AS total_jobs

    FROM
        {db.gold_table("jobs")}

    GROUP BY
        employment_type

    ORDER BY
        total_jobs DESC
    """

    return db.dataframe(query)


def open_vs_closed_jobs():

    query = f"""
    SELECT

        status,

        COUNT(*) AS total_jobs

    FROM
        {db.gold_table("jobs")}

    GROUP BY
        status
    """

    return db.dataframe(query)


def vacancies_by_department():

    query = f"""
    SELECT

        department,

        SUM(vacancies) AS total_vacancies

    FROM
        {db.gold_table("jobs")}

    GROUP BY
        department

    ORDER BY
        total_vacancies DESC
    """

    return db.dataframe(query)


def average_salary_by_department():

    query = f"""
    SELECT

        department,

        ROUND(AVG(min_salary),2) AS avg_min_salary,

        ROUND(AVG(max_salary),2) AS avg_max_salary

    FROM
        {db.gold_table("jobs")}

    GROUP BY
        department

    ORDER BY
        avg_max_salary DESC
    """

    return db.dataframe(query)


def experience_required():

    query = f"""
    SELECT

        job_title,

        min_experience,

        max_experience

    FROM
        {db.gold_table("jobs")}

    ORDER BY
        max_experience DESC
    """

    return db.dataframe(query)


def top_paying_jobs(limit=10):

    query = f"""
    SELECT

        job_title,

        location,

        min_salary,

        max_salary

    FROM
        {db.gold_table("jobs")}

    ORDER BY
        max_salary DESC

    LIMIT {limit}
    """

    return db.dataframe(query)


def job_summary():

    query = f"""
    SELECT

        job_title,

        department,

        location,

        vacancies,

        status

    FROM
        {db.gold_table("jobs")}
    """

    return db.dataframe(query)