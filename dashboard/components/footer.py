"""
==========================================================
TalentFlow AI
Footer Component
==========================================================
"""

from datetime import datetime

import streamlit as st


def render_footer():

    st.divider()

    left, middle, right = st.columns(3)

    with left:

        st.caption("🚀 TalentFlow AI")

        st.caption("AI Recruitment Intelligence Platform")

    with middle:

        st.caption("Version")

        st.caption("v1.0.0")

    with right:

        st.caption("Last Refresh")

        st.caption(

            datetime.now().strftime(

                "%d %b %Y %I:%M %p"

            )

        )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.success("🟢 PostgreSQL")

    with col2:

        st.success("🟢 DuckDB")

    with col3:

        st.success("🟢 Analytics")

    with col4:

        st.success("🟢 ETL Pipeline")

    st.caption(

        "Built using FastAPI • PostgreSQL • DuckDB • Streamlit • Plotly"

    )