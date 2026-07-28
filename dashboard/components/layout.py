"""
==========================================================
TalentFlow AI
Layout Engine
==========================================================

Purpose:
Reusable layout helpers used across all dashboard pages.

This file DOES NOT contain styling.
Styling belongs only to theme.css.
"""

import streamlit as st


# ==========================================================
# PAGE TITLE
# ==========================================================

def page_title(
    title: str,
    subtitle: str = "",
):
    """
    Render a standard page title.
    """

    st.title(title)

    if subtitle:
        st.caption(subtitle)


# ==========================================================
# SECTION TITLE
# ==========================================================

def section_title(
    title: str,
    business_question: str = "",
):
    """
    Render a section heading.
    """

    st.subheader(title)

    if business_question:
        st.caption(
            f"📌 Business Question: {business_question}"
        )


# ==========================================================
# STANDARD SPACING
# ==========================================================

def spacer(
    lines: int = 1,
):
    """
    Add vertical spacing.
    """

    for _ in range(lines):
        st.write("")


# ==========================================================
# DIVIDER
# ==========================================================

def divider():
    """
    Standard divider.
    """

    st.divider()


# ==========================================================
# CONTAINERS
# ==========================================================

def container(
    border: bool = False,
):
    """
    Standard Streamlit container.
    """

    return st.container(
        border=border
    )


# ==========================================================
# GRID LAYOUTS
# ==========================================================

def two_columns(
    left_ratio=1,
    right_ratio=1,
    gap="large",
):

    return st.columns(
        [left_ratio, right_ratio],
        gap=gap,
    )


def three_columns(
    gap="large",
):

    return st.columns(
        3,
        gap=gap,
    )


def four_columns(
    gap="medium",
):

    return st.columns(
        4,
        gap=gap,
    )


def five_columns(
    gap="small",
):

    return st.columns(
        5,
        gap=gap,
    )


# ==========================================================
# EXECUTIVE KPI GRID
# ==========================================================

def executive_kpi_grid():
    """
    Standard KPI layout
    (4 KPI cards)
    """

    return st.columns(
        4,
        gap="medium",
    )


# ==========================================================
# EXECUTIVE CHART GRID
# ==========================================================

def executive_chart_grid():
    """
    Two equal charts
    """

    return st.columns(
        2,
        gap="large",
    )


# ==========================================================
# SUMMARY + ALERT GRID
# ==========================================================

def summary_alert_grid():
    """
    AI Summary + Alerts
    """

    return st.columns(
        [2, 1],
        gap="large",
    )


# ==========================================================
# FULL WIDTH
# ==========================================================

def full_width():
    """
    Placeholder for semantic clarity.
    """

    return st.container()


# ==========================================================
# DECISION CENTER
# ==========================================================

def decision_center():
    """
    Full width decision panel.
    """

    return st.container()