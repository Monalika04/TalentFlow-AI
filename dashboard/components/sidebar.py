"""
==========================================================
TalentFlow AI
Sidebar Component
==========================================================

Purpose:
Reusable navigation sidebar used across all dashboard pages.
"""

import streamlit as st


def render_sidebar():
    """
    Render TalentFlow AI sidebar.
    """

    with st.sidebar:

        # ==================================================
        # BRANDING
        # ==================================================

        st.markdown("# 🤖 TalentFlow AI")

        st.caption(
            "AI Recruitment Intelligence Platform"
        )

        st.divider()

        # ==================================================
        # WORKSPACES
        # ==================================================

        st.markdown("### 📂 Workspaces")

        st.page_link(
            "Home.py",
            label="🏠 Home",
        )

        st.page_link(
            "pages/1_Executive.py",
            label="📊 Executive Overview",
        )

        st.page_link(
            "pages/2_Talent.py",
            label="👥 Talent Intelligence",
        )

        st.page_link(
            "pages/3_Hiring.py",
            label="💼 Hiring Operations",
        )

        st.page_link(
            "pages/4_Pipeline.py",
            label="📄 Recruitment Pipeline",
        )

        st.page_link(
            "pages/5_AI_Intelligence.py",
            label="🤖 AI Intelligence",
        )

        st.page_link(
            "pages/6_Decision_Center.py",
            label="🎯 Decision Center",
        )

        st.page_link(
            "pages/7_Reports.py",
            label="📑 Reports",
        )

        st.page_link(
            "pages/8_Copilot.py",
            label="💬 TalentFlow Copilot",
        )

        st.divider()

        # ==================================================
        # SYSTEM STATUS
        # ==================================================

        st.markdown("### ⚙️ System Status")

        col1, col2 = st.columns([1, 4])

        with col1:
            st.success("●")

        with col2:
            st.caption("PostgreSQL Connected")

        col1, col2 = st.columns([1, 4])

        with col1:
            st.success("●")

        with col2:
            st.caption("Warehouse Ready")

        col1, col2 = st.columns([1, 4])

        with col1:
            st.success("●")

        with col2:
            st.caption("Analytics Ready")

        st.divider()

        # ==================================================
        # VERSION
        # ==================================================

        st.caption("TalentFlow AI")

        st.caption("Version 1.0.0")

        st.caption("Built with ❤️ using")

        st.caption(
            "FastAPI • PostgreSQL • DuckDB • Streamlit"
        )