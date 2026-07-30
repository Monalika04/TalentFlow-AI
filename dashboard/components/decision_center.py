"""
==========================================================
TalentFlow AI
Executive Decision Center
==========================================================
"""

import streamlit as st


PRIORITY_COLOR = {

    "Critical": "🔴",

    "High": "🟠",

    "Medium": "🟡",

    "Low": "🟢",

}


def render_decision_center(
    decisions,
):
    """
    Parameters
    ----------
    decisions : list[dict]

    Example
    -------
    [
        {
            "priority":"Critical",
            "title":"Increase Backend Hiring",
            "reason":"18 open backend vacancies",
            "action":"Assign recruiters immediately"
        }
    ]
    """

    st.subheader("🎯 Executive Decision Center")

    st.caption(
        "AI-powered recruitment recommendations based on current analytics."
    )

    st.divider()

    if not decisions:

        st.success(
            "No critical business decisions required today."
        )

        return

    for decision in decisions:

        icon = PRIORITY_COLOR.get(
            decision["priority"],
            "⚪",
        )

        with st.container(border=True):

            left, right = st.columns([5, 1])

            with left:

                st.markdown(
                    f"### {icon} {decision['title']}"
                )

                st.write(
                    decision["reason"]
                )

                st.caption(
                    f"Recommended Action: {decision['action']}"
                )

            with right:

                st.metric(

                    label="Priority",

                    value=decision["priority"],

                )