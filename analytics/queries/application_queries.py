from analytics.database import db


def applications_by_status():

    query = f"""
    SELECT

        application_status,

        COUNT(*) AS total_applications

    FROM
        {db.gold_table("applications")}

    GROUP BY
        application_status

    ORDER BY
        total_applications DESC
    """

    return db.dataframe(query)


def applications_by_source():

    query = f"""
    SELECT

        source,

        COUNT(*) AS total_applications

    FROM
        {db.gold_table("applications")}

    GROUP BY
        source

    ORDER BY
        total_applications DESC
    """

    return db.dataframe(query)


def applications_by_month():

    query = f"""
    SELECT

        strftime(application_date,'%Y-%m') AS month,

        COUNT(*) AS total_applications

    FROM
        {db.gold_table("applications")}

    GROUP BY
        month

    ORDER BY
        month
    """

    return db.dataframe(query)


def applications_by_candidate():

    query = f"""
    SELECT

        candidate_id,

        COUNT(*) AS applications

    FROM
        {db.gold_table("applications")}

    GROUP BY
        candidate_id

    ORDER BY
        applications DESC
    """

    return db.dataframe(query)


def applications_by_job():

    query = f"""
    SELECT

        job_id,

        COUNT(*) AS applications

    FROM
        {db.gold_table("applications")}

    GROUP BY
        job_id

    ORDER BY
        applications DESC
    """

    return db.dataframe(query)


def ai_match_distribution():

    query = f"""
    SELECT

        ai_match_score

    FROM
        {db.gold_table("applications")}

    WHERE
        ai_match_score IS NOT NULL
    """

    return db.dataframe(query)


def recruiter_notes():

    query = f"""
    SELECT

        application_id,

        recruiter_notes

    FROM
        {db.gold_table("applications")}

    WHERE
        recruiter_notes IS NOT NULL
    """

    return db.dataframe(query)


def application_summary():

    query = f"""
    SELECT

        application_id,

        candidate_id,

        job_id,

        application_status,

        ai_match_score,

        source

    FROM
        {db.gold_table("applications")}
    """

    return db.dataframe(query)


def average_match_score():

    query = f"""
    SELECT

        ROUND(
            AVG(ai_match_score),
            2
        ) AS average_score

    FROM
        {db.gold_table("applications")}
    """

    return db.dataframe(query)


def highest_match_candidates(limit=10):

    query = f"""
    SELECT

        application_id,

        candidate_id,

        job_id,

        ai_match_score

    FROM
        {db.gold_table("applications")}

    WHERE
        ai_match_score IS NOT NULL

    ORDER BY
        ai_match_score DESC

    LIMIT {limit}
    """

    return db.dataframe(query)