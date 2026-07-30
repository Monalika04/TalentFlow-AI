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

    # Executive Dashboard
    applications_by_source,
    ai_score_distribution,
    application_aging,
    monthly_application_trend,
    priority_jobs,
    top_ai_candidates,
    hiring_funnel,
    recruitment_health,
)


class ExecutiveService:

    @staticmethod
    def get_dashboard_metrics():
        return {
            "total_candidates": int(total_candidates().iloc[0, 0]),
            "total_jobs": int(total_jobs().iloc[0, 0]),
            "total_companies": int(total_companies().iloc[0, 0]),
            "total_applications": int(total_applications().iloc[0, 0]),
            "open_jobs": int(open_jobs().iloc[0, 0]),
            "closed_jobs": int(closed_jobs().iloc[0, 0]),
            "active_candidates": int(active_candidates().iloc[0, 0]),
            "inactive_candidates": int(inactive_candidates().iloc[0, 0]),
            "average_experience": float(average_experience().iloc[0, 0]),
            "average_current_ctc": float(average_current_ctc().iloc[0, 0]),
            "average_expected_ctc": float(average_expected_ctc().iloc[0, 0]),
            "average_ai_match_score": float(average_ai_match_score().iloc[0, 0]),
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

    # ==========================================================
    # EXECUTIVE DASHBOARD
    # ==========================================================

    @staticmethod
    def get_hiring_funnel():
        return hiring_funnel()

    @staticmethod
    def get_application_sources():
        return applications_by_source()

    @staticmethod
    def get_ai_score_distribution():
        return ai_score_distribution()

    @staticmethod
    def get_application_aging():
        return application_aging()

    @staticmethod
    def get_monthly_application_trend():
        return monthly_application_trend()

    @staticmethod
    def get_priority_jobs():
        return priority_jobs()

    @staticmethod
    def get_top_ai_candidates():
        return top_ai_candidates()

    @staticmethod
    def get_recruitment_health():
        return recruitment_health()

    # ==========================================================
    # COMPLETE EXECUTIVE DASHBOARD DATA
    # ==========================================================

    @staticmethod
    def get_executive_dashboard():
        return {
            "metrics": ExecutiveService.get_dashboard_metrics(),
            "application_status": ExecutiveService.get_application_status(),
            "jobs_by_department": ExecutiveService.get_jobs_by_department(),
            "companies_by_industry": ExecutiveService.get_companies_by_industry(),
            "hiring_funnel": ExecutiveService.get_hiring_funnel(),
            "application_sources": ExecutiveService.get_application_sources(),
            "ai_score_distribution": ExecutiveService.get_ai_score_distribution(),
            "application_aging": ExecutiveService.get_application_aging(),
            "monthly_trend": ExecutiveService.get_monthly_application_trend(),
            "priority_jobs": ExecutiveService.get_priority_jobs(),
            "top_ai_candidates": ExecutiveService.get_top_ai_candidates(),
            "recruitment_health": ExecutiveService.get_recruitment_health(),
            "health_score":
            ExecutiveService.get_health_score(),
            "executive_summary":
    ExecutiveService.get_executive_summary(),
            "decision_center":
    ExecutiveService.get_decision_center(),
            "forecast":
    ExecutiveService.get_forecast(),
        }
        
    @staticmethod
    def get_alerts():

            alerts = []

            metrics = ExecutiveService.get_dashboard_metrics()

            if metrics["average_ai_match_score"] < 70:

                alerts.append(

                    {

                        "severity":"Warning",

                        "title":"Low AI Match Score",

                        "message":"Average AI score dropped below 70%.",

                    }

                )

            if metrics["open_jobs"] > metrics["closed_jobs"]:

                alerts.append(

                    {

                        "severity":"Critical",

                        "title":"Hiring Backlog",

                        "message":"Open jobs exceed closed jobs.",

                    }

                )

            if metrics["inactive_candidates"] > metrics["active_candidates"]:

                alerts.append(

                    {

                        "severity":"Info",

                        "title":"Candidate Engagement",

                        "message":"Inactive candidates exceed active candidates.",

                    }

                )

            return alerts
        
        
    
    # ==========================================================
# HEALTH SCORE
# ==========================================================

@staticmethod
def get_health_score():

    metrics = ExecutiveService.get_dashboard_metrics()

    score = 100

    # Average AI Match Score (40%)

    ai_score = metrics["average_ai_match_score"]

    score = score - max(0, 80 - ai_score) * 0.40

    # Open Jobs vs Closed Jobs (30%)

    if metrics["open_jobs"] > metrics["closed_jobs"]:

        score -= 10

    # Active Candidates (20%)

    if metrics["active_candidates"] < metrics["inactive_candidates"]:

        score -= 10

    # Applications (10%)

    if metrics["total_applications"] < metrics["total_jobs"]:

        score -= 5

    score = max(0, min(round(score), 100))

    if score >= 85:

        status = "Healthy"

    elif score >= 70:

        status = "Warning"

    else:

        status = "Critical"

    return {

        "score": score,

        "status": status,

    }
    
# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

@staticmethod
def get_executive_summary():

    metrics = ExecutiveService.get_dashboard_metrics()

    insights = []

    recommendations = []

    insights.append(

        f"Total applications received: {metrics['total_applications']}."

    )

    insights.append(

        f"Open jobs: {metrics['open_jobs']}."

    )

    insights.append(

        f"Average AI Match Score: {metrics['average_ai_match_score']}%."

    )

    if metrics["average_ai_match_score"] >= 80:

        insights.append(

            "AI recommendation quality is performing well."

        )

    else:

        insights.append(

            "AI recommendation quality requires attention."

        )

    if metrics["open_jobs"] > metrics["closed_jobs"]:

        recommendations.append(

            "Prioritize closing open job positions."

        )

    recommendations.append(

        "Schedule interviews for shortlisted candidates."

    )

    recommendations.append(

        "Review applications pending screening."

    )

    recommendations.append(

        "Increase sourcing for high-demand roles."

    )

    return {

        "insights": insights,

        "recommendations": recommendations,

    }
    
    

# ==========================================================
# DECISION CENTER
# ==========================================================

@staticmethod
def get_decision_center():

    metrics = ExecutiveService.get_dashboard_metrics()

    decisions = []

    if metrics["open_jobs"] > metrics["closed_jobs"]:

        decisions.append({

            "priority":"Critical",

            "title":"Reduce Hiring Backlog",

            "reason":(
                f"{metrics['open_jobs']} open jobs "
                "are waiting to be filled."
            ),

            "action":"Assign additional recruiters to open positions.",

        })

    if metrics["average_ai_match_score"] < 80:

        decisions.append({

            "priority":"High",

            "title":"Improve AI Match Quality",

            "reason":"Average AI Match Score is below target.",

            "action":"Review matching rules and candidate screening.",

        })

    if metrics["inactive_candidates"] > metrics["active_candidates"]:

        decisions.append({

            "priority":"Medium",

            "title":"Re-engage Candidate Pool",

            "reason":"Inactive candidates exceed active candidates.",

            "action":"Launch email and recruiter outreach campaigns.",

        })

    if metrics["average_experience"] < 3:

        decisions.append({

            "priority":"Low",

            "title":"Attract Senior Talent",

            "reason":"Average candidate experience is relatively low.",

            "action":"Increase sourcing for senior-level professionals.",

        })

    return decisions

@staticmethod
def get_forecast():

    metrics = ExecutiveService.get_dashboard_metrics()

    forecast = {

        "applications": "Growing"
            if metrics["total_applications"] > metrics["total_jobs"]
            else "Stable",

        "candidate_pool": "Healthy"
            if metrics["active_candidates"] >= metrics["inactive_candidates"]
            else "Needs Attention",

        "ai_quality": "Improving"
            if metrics["average_ai_match_score"] >= 80
            else "Monitor",

        "job_demand": "High"
            if metrics["open_jobs"] > metrics["closed_jobs"]
            else "Balanced",

        "hiring_velocity": "Good"
            if metrics["average_experience"] >= 3
            else "Slow",

    }

    insights = []

    if forecast["job_demand"] == "High":
        insights.append(
            "Backend hiring demand is expected to remain high."
        )

    if forecast["ai_quality"] == "Improving":
        insights.append(
            "AI recommendation quality is performing consistently."
        )

    if forecast["candidate_pool"] == "Needs Attention":
        insights.append(
            "Increase candidate sourcing campaigns."
        )

    if not insights:
        insights.append(
            "Recruitment pipeline is expected to remain stable."
        )

    return {

        "forecast": forecast,

        "insights": insights,

    }