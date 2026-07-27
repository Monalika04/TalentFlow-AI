from analytics.database import db


def candidate_job_ai_analysis():

    query = f"""

    SELECT

        a.application_id,

        c.candidate_id,

        CONCAT(

            c.first_name,

            ' ',

            c.last_name

        ) AS candidate_name,

        j.job_title,

        j.department,

        j.location,

        co.company_name,

        c.city,

        c.highest_education,

        c.total_experience,

        c.current_ctc,

        c.expected_ctc,

        a.application_status,

        a.source,

        a.ai_match_score,

        r.overall_score,

        r.skill_score,

        r.experience_score,

        r.education_score,

        r.confidence_score,

        r.recommendation,

        r.hiring_priority

    FROM

        {db.gold_table("applications")} a

    LEFT JOIN

        {db.gold_table("candidates")} c

    ON

        a.candidate_id = c.candidate_id

    LEFT JOIN

        {db.gold_table("jobs")} j

    ON

        a.job_id = j.job_id

    LEFT JOIN

        {db.gold_table("companies")} co

    ON

        j.company_id = co.company_id

    LEFT JOIN

        {db.gold_table("recommendations")} r

    ON

        a.application_id = r.application_id

    """

    return db.dataframe(query)