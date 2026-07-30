"""
==========================================================
TalentFlow AI
Executive Hiring Health Component
==========================================================
"""

import streamlit as st


STATUS_CLASS = {
    "Healthy": "tf-chip-success",
    "Warning": "tf-chip-warning",
    "Critical": "tf-chip-danger",
}


def render_health_score(
    score: float,
    status: str,
    summary: str,
    recommendation: str,
):
    """
    Executive Hiring Health Hero Banner.

    Parameters
    ----------
    score : float
        Overall hiring health (0-100)

    status : str
        Healthy | Warning | Critical

    summary : str
        AI generated summary

    recommendation : str
        Business recommendation
    """

    status_class = STATUS_CLASS.get(
        status,
        "tf-chip-success",
    )

    left, right = st.columns([3, 1])

    with left:

        st.markdown(
            f"""
<div class="tf-hero">

<h2 style="margin-bottom:8px;">
🏆 Recruitment Health Score
</h2>

<p style="font-size:54px;
font-weight:700;
margin-top:0;
margin-bottom:10px;">

{score:.0f}%

</p>

<span class="tf-chip {status_class}">
{status}
</span>

<br><br>

<h4>📌 Executive Summary</h4>

<p>{summary}</p>

<h4>🎯 Recommended Action</h4>

<p>{recommendation}</p>

</div>
""",
            unsafe_allow_html=True,
        )

    with right:

        st.metric(

            label="Hiring Health",

            value=f"{score:.0f}%",

        )

        st.progress(score / 100)

        st.write("")

        if score >= 85:

            st.success("Excellent")

        elif score >= 70:

            st.warning("Needs Attention")

        else:

            st.error("Critical")