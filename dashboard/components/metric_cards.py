"""
==========================================================
TalentFlow AI
Enterprise KPI Cards
==========================================================

This component is responsible only for rendering KPI cards.

Business values come from:
Analytics Service

Metadata comes from:
kpi_config.py
"""

import streamlit as st

from dashboard.components.progress import render_progress


STATUS_CLASS = {
    "Healthy": "tf-chip-success",
    "Warning": "tf-chip-warning",
    "Critical": "tf-chip-danger",
}


def metric_card(
    title: str,
    value,
    icon: str,
    trend: str,
    progress: float,
    status: str,
    description: str,
):
    """
    Render a single KPI card.
    """

    status_class = STATUS_CLASS.get(
        status,
        "tf-chip-success",
    )

    st.markdown(
        f"""
        <div class="tf-kpi-card">

            <div class="tf-kpi-header">

                <div>

                    <div style="font-size:28px;">
                        {icon}
                    </div>

                    <div class="tf-kpi-title">
                        {title}
                    </div>

                </div>

                <div style="
                    font-size:14px;
                    font-weight:600;
                    color:#22C55E;
                ">
                    {trend}
                </div>

            </div>

            <div class="tf-kpi-value">
                {value}
            </div>

            <span class="tf-chip {status_class}">
                {status}
            </span>

        </div>
        """,
        unsafe_allow_html=True,
    )

    render_progress(progress)

    st.caption(description)


def render_kpis(
    configuration: list,
    values: dict,
):
    """
    Render KPI cards from configuration + analytics values.

    Parameters
    ----------
    configuration : list
        Metadata from kpi_config.py

    values : dict
        KPI values returned by ExecutiveService
    """

    columns = st.columns(
        len(configuration),
        gap="medium",
    )

    for column, config in zip(columns, configuration):

        metric = values.get(config["id"])

        if metric is None:
            continue

        with column:

            metric_card(

                title=config["title"],

                icon=config["icon"],

                value=metric["value"],

                trend=metric["trend"],

                progress=metric["progress"],

                status=metric["status"],

                description=metric["description"],

            )