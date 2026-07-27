from analytics.database import db


def candidates_by_city():

    query = f"""
    SELECT

        city,

        COUNT(*) AS total_candidates

    FROM
        {db.gold_table("candidates")}

    GROUP BY
        city

    ORDER BY
        total_candidates DESC
    """

    return db.dataframe(query)


def candidates_by_state():

    query = f"""
    SELECT

        state,

        COUNT(*) AS total_candidates

    FROM
        {db.gold_table("candidates")}

    GROUP BY
        state

    ORDER BY
        total_candidates DESC
    """

    return db.dataframe(query)


def candidates_by_country():

    query = f"""
    SELECT

        country,

        COUNT(*) AS total_candidates

    FROM
        {db.gold_table("candidates")}

    GROUP BY
        country

    ORDER BY
        total_candidates DESC
    """

    return db.dataframe(query)


def candidates_by_status():

    query = f"""
    SELECT

        status,

        COUNT(*) AS total_candidates

    FROM
        {db.gold_table("candidates")}

    GROUP BY
        status
    """

    return db.dataframe(query)


def education_distribution():

    query = f"""
    SELECT

        highest_education,

        COUNT(*) AS total_candidates

    FROM
        {db.gold_table("candidates")}

    GROUP BY
        highest_education

    ORDER BY
        total_candidates DESC
    """

    return db.dataframe(query)


def experience_distribution():

    query = f"""
    SELECT

        total_experience,

        COUNT(*) AS total_candidates

    FROM
        {db.gold_table("candidates")}

    GROUP BY
        total_experience

    ORDER BY
        total_experience
    """

    return db.dataframe(query)


def notice_period_distribution():

    query = f"""
    SELECT

        notice_period_days,

        COUNT(*) AS total_candidates

    FROM
        {db.gold_table("candidates")}

    GROUP BY
        notice_period_days

    ORDER BY
        notice_period_days
    """

    return db.dataframe(query)


def salary_distribution():

    query = f"""
    SELECT

        current_ctc,
        expected_ctc

    FROM
        {db.gold_table("candidates")}
    """

    return db.dataframe(query)


def top_experienced_candidates(limit=10):

    query = f"""
    SELECT

        candidate_id,

        first_name,

        last_name,

        city,

        total_experience,

        current_ctc,

        expected_ctc

    FROM
        {db.gold_table("candidates")}

    ORDER BY
        total_experience DESC

    LIMIT {limit}
    """

    return db.dataframe(query)


def candidate_locations():

    query = f"""
    SELECT

        city,

        state,

        country,

        COUNT(*) AS total_candidates

    FROM
        {db.gold_table("candidates")}

    GROUP BY

        city,
        state,
        country

    ORDER BY
        total_candidates DESC
    """

    return db.dataframe(query)