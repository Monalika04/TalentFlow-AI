"""
==========================================================
TalentFlow AI
Enterprise Table Components
==========================================================

Reusable table components for all dashboard pages.
"""

import streamlit as st
import pandas as pd


# ==========================================================
# STANDARD TABLE
# ==========================================================

def render_table(
    data: pd.DataFrame,
    title: str,
    height: int = 400,
):
    """
    Render a responsive enterprise table.
    """

    st.subheader(title)

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True,
        height=height,
    )


# ==========================================================
# PRIORITY JOBS
# ==========================================================

def priority_jobs_table(
    data: pd.DataFrame,
):
    """
    Display high priority open jobs.
    """

    st.subheader("📋 Priority Open Jobs")

    st.caption(
        "Jobs requiring immediate recruiter attention."
    )

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True,
        height=350,
    )


# ==========================================================
# TOP AI CANDIDATES
# ==========================================================

def top_ai_candidates_table(
    data: pd.DataFrame,
):
    """
    Display top AI matched candidates.
    """

    st.subheader("🤖 Top AI Recommended Candidates")

    st.caption(
        "Highest AI Match Score candidates."
    )

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True,
        height=350,
    )


# ==========================================================
# DOWNLOAD BUTTON
# ==========================================================

def export_csv(
    data: pd.DataFrame,
    filename: str,
):
    """
    Export dataframe as CSV.
    """

    st.download_button(

        label="📥 Export CSV",

        data=data.to_csv(index=False),

        file_name=f"{filename}.csv",

        mime="text/csv",

    )