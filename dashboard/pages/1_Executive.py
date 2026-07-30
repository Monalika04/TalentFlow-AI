"""
==========================================================
TalentFlow AI
Executive Dashboard
==========================================================
"""

from dashboard.components.theme import (
    configure_page,
    load_theme,
)

from dashboard.components.header import (
    render_header,
)

from dashboard.components.sidebar import (
    render_sidebar,
)

from dashboard.components.filters import (
    render_filters,
)

from dashboard.components.health_score import (
    render_health_score,
)

from dashboard.components.metric_cards import (
    render_kpis,
)

from dashboard.components.kpi_config import (
    EXECUTIVE_KPIS,
)

from dashboard.components.executive_summary import (
    render_executive_summary,
)

from dashboard.components.alerts import (
    render_alerts,
)

from dashboard.components.charts import (
    hiring_funnel_chart,
    horizontal_bar_chart,
    donut_chart,
    area_chart,
)

from dashboard.components.tables import (
    priority_jobs_table,
    top_ai_candidates_table,
)

from analytics.services.executive_service import (
    ExecutiveService,
)
from dashboard.components.decision_center import (
    render_decision_center,
)

from dashboard.components.footer import (
    render_footer,
)

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

configure_page("Executive Dashboard")

load_theme()

render_sidebar()

render_header(

    page_title="Executive Overview",

    page_description="Monitor recruitment performance, hiring health, and executive KPIs."

)


# ==========================================================
# FILTERS
# ==========================================================

filters = render_filters()


# ==========================================================
# LOAD DASHBOARD DATA
# ==========================================================

dashboard = ExecutiveService.get_executive_dashboard()


# ==========================================================
# HEALTH SCORE
# ==========================================================

health = dashboard["recruitment_health"]

health = dashboard["health_score"]

render_health_score(

    score=health["score"],

    status=health["status"],

    summary="""
Recruitment pipeline is healthy.
AI recommendation quality remains strong.
""",

    recommendation="""
Increase sourcing for Backend Engineers.
""",

)


# ==========================================================
# KPI CARDS
# ==========================================================

render_kpis(

    EXECUTIVE_KPIS,

    dashboard["metrics"],

)


# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================
# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

summary = dashboard["executive_summary"]

render_executive_summary(

    insights=summary["insights"],

    recommendations=summary["recommendations"],

)


# ==========================================================
# ALERTS
# ==========================================================

render_alerts(

    dashboard["alerts"]

)


# ==========================================================
# CHARTS - ROW 1
# ==========================================================

left, right = __import__("streamlit").columns(2)

with left:

    hiring_funnel_chart(

        dashboard["hiring_funnel"]

    )

with right:

    horizontal_bar_chart(

        dashboard["jobs_by_department"],

        x="total_jobs",

        y="department",

        title="Department Hiring Demand",

    )


# ==========================================================
# CHARTS - ROW 2
# ==========================================================

left, right = __import__("streamlit").columns(2)

with left:

    donut_chart(

        dashboard["application_sources"],

        names="source",

        values="total_applications",

        title="Recruitment Sources",

    )

with right:

    donut_chart(

        dashboard["ai_score_distribution"],

        names="score_band",

        values="total",

        title="AI Match Score Distribution",

    )


# ==========================================================
# CHARTS - ROW 3
# ==========================================================

left, right = __import__("streamlit").columns(2)

with left:

    area_chart(

        dashboard["monthly_trend"],

        x="application_month",

        y="total_applications",

        title="Monthly Hiring Trend",

    )

with right:

    donut_chart(

        dashboard["application_aging"],

        names="application_bucket",

        values="total",

        title="Application Aging",

    )


# ==========================================================
# TABLES
# ==========================================================

priority_jobs_table(

    dashboard["priority_jobs"]

)

top_ai_candidates_table(

    dashboard["top_ai_candidates"]

)


render_decision_center(

    dashboard["decision_center"]

)

render_footer()

from dashboard.components.executive_forecast import (
    render_forecast,
)

render_forecast(
    dashboard["forecast"]
)