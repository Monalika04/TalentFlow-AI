"""
==========================================================
TalentFlow AI
Executive Alerts Component
==========================================================
"""

import streamlit as st


SEVERITY = {

    "Critical": "🔴",

    "Warning": "🟡",

    "Info": "🔵",

}


def render_alerts(alerts):

    """
    Parameters
    ----------
    alerts : list[dict]

    Example

    [

        {

            "severity":"Critical",

            "title":"Backend Hiring",

            "message":"Backend vacancies increased to 18."

        }

    ]
    """

    st.subheader("🚨 Executive Alerts")

    st.caption(
        "Critical recruitment events requiring attention."
    )

    st.divider()

    if len(alerts) == 0:

        st.success(
            "No active alerts."
        )

        return

    for alert in alerts:

        severity = alert["severity"]

        icon = SEVERITY.get(
            severity,
            "⚪",
        )

        with st.container(border=True):

            col1, col2 = st.columns(
                [1, 9]
            )

            with col1:

                st.markdown(
                    f"# {icon}"
                )

            with col2:

                st.markdown(
                    f"**{alert['title']}**"
                )

                st.write(
                    alert["message"]
                )