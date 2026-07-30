"""
==========================================================
TalentFlow AI
Global Filter Component
==========================================================

Purpose:
Reusable filters used across all dashboard pages.
"""

from datetime import date, timedelta

import streamlit as st


def render_filters():

    st.markdown("### 🔍 Global Filters")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        company = st.selectbox(

            "Company",

            [
                "All",
                "Google",
                "Microsoft",
                "Amazon",
                "Meta",
            ],

        )

    with col2:

        department = st.selectbox(

            "Department",

            [
                "All",
                "Engineering",
                "Data",
                "HR",
                "Marketing",
                "Finance",
            ],

        )

    with col3:

        location = st.selectbox(

            "Location",

            [
                "All",
                "Mumbai",
                "Bangalore",
                "Pune",
                "Hyderabad",
                "Remote",
            ],

        )

    with col4:

        recruiter = st.selectbox(

            "Recruiter",

            [
                "All",
                "Recruiter A",
                "Recruiter B",
                "Recruiter C",
            ],

        )

    col5, col6 = st.columns([2, 1])

    with col5:

        date_range = st.date_input(

            "Date Range",

            value=(
                date.today() - timedelta(days=30),
                date.today(),
            ),

        )

    with col6:

        st.markdown("<br>", unsafe_allow_html=True)

        apply = st.button(

            "Apply Filters",

            use_container_width=True,

            type="primary",

        )

    st.divider()

    return {

        "company": company,

        "department": department,

        "location": location,

        "recruiter": recruiter,

        "date_range": date_range,

        "apply": apply,

    }