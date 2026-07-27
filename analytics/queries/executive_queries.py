from analytics.database import db


def total_candidates():

    query = f"""
    SELECT

        COUNT(*) AS total_candidates

    FROM
        {db.gold_table("candidates")}
    """

    return db.dataframe(query)


def total_jobs():

    query = f"""
    SELECT

        COUNT(*) AS total_jobs

    FROM
        {db.gold_table("jobs")}
    """

    return db.dataframe(query)


def total_companies():

    query = f"""
    SELECT

        COUNT(*) AS total_companies

    FROM
        {db.gold_table("companies")}
    """

    return db.dataframe(query)


def total_applications():

    query = f"""
    SELECT

        COUNT(*) AS total_applications

    FROM
        {db.gold_table("applications")}
    """

    return db.dataframe(query)


def open_jobs():

    query = f"""
    SELECT

        COUNT(*) AS open_jobs

    FROM
        {db.gold_table("jobs")}

    WHERE

        status='OPEN'
    """

    return db.dataframe(query)


def closed_jobs():

    query = f"""
    SELECT

        COUNT(*) AS closed_jobs

    FROM
        {db.gold_table("jobs")}

    WHERE

        status='CLOSED'
    """

    return db.dataframe(query)


def active_candidates():

    query = f"""
    SELECT

        COUNT(*) AS active_candidates

    FROM
        {db.gold_table("candidates")}

    WHERE

        status='ACTIVE'
    """

    return db.dataframe(query)


def inactive_candidates():

    query = f"""
    SELECT

        COUNT(*) AS inactive_candidates

    FROM
        {db.gold_table("candidates")}

    WHERE

        status='INACTIVE'
    """

    return db.dataframe(query)


def average_experience():

    query = f"""
    SELECT

        ROUND(
            AVG(total_experience),
            2
        ) AS average_experience

    FROM
        {db.gold_table("candidates")}
    """

    return db.dataframe(query)


def average_current_ctc():

    query = f"""
    SELECT

        ROUND(
            AVG(current_ctc),
            2
        ) AS average_current_ctc

    FROM
        {db.gold_table("candidates")}
    """

    return db.dataframe(query)


def average_expected_ctc():

    query = f"""
    SELECT

        ROUND(
            AVG(expected_ctc),
            2
        ) AS average_expected_ctc

    FROM
        {db.gold_table("candidates")}
    """

    return db.dataframe(query)


def average_ai_match_score():

    query = f"""
    SELECT

        ROUND(
            AVG(ai_match_score),
            2
        ) AS average_ai_match_score

    FROM
        {db.gold_table("applications")}
    """

    return db.dataframe(query)


def applications_by_status():

    query = f"""
    SELECT

        application_status,

        COUNT(*) AS total

    FROM

        {db.gold_table("applications")}

    GROUP BY

        application_status

    ORDER BY

        total DESC
    """

    return db.dataframe(query)


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


def companies_by_industry():

    query = f"""
    SELECT

        industry,

        COUNT(*) AS total_companies

    FROM

        {db.gold_table("companies")}

    GROUP BY

        industry

    ORDER BY

        total_companies DESC
    """

    return db.dataframe(query)