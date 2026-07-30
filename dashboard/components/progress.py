"""
==========================================================
TalentFlow AI
Progress Component
==========================================================

Reusable enterprise progress bar.
"""

import streamlit as st


def render_progress(progress: float):
    """
    Render KPI progress bar.

    Parameters
    ----------
    progress : float
        Value between 0 and 100.
    """

    progress = max(0, min(float(progress), 100))

    st.markdown(
        f"""
        <div class="tf-progress">
            <div
                class="tf-progress-fill"
                style="width:{progress}%;">
            </div>
        </div>

        <div style="
            margin-top:6px;
            font-size:12px;
            color:#94A3B8;
            text-align:right;
        ">
            {progress:.0f}% of Target
        </div>
        """,
        unsafe_allow_html=True,
    )