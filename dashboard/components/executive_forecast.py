import streamlit as st


def render_forecast(data):

    st.subheader("📈 Executive Snapshot & Forecast")

    st.caption(
        "Expected recruitment outlook based on current business metrics."
    )

    left, right = st.columns([1, 1])

    with left:

        st.metric(
            "Applications",
            data["forecast"]["applications"],
        )

        st.metric(
            "Candidate Pool",
            data["forecast"]["candidate_pool"],
        )

        st.metric(
            "AI Quality",
            data["forecast"]["ai_quality"],
        )

        st.metric(
            "Job Demand",
            data["forecast"]["job_demand"],
        )

        st.metric(
            "Hiring Velocity",
            data["forecast"]["hiring_velocity"],
        )

    with right:

        st.markdown("### 💡 Business Forecast")

        for item in data["insights"]:

            st.markdown(f"• {item}")