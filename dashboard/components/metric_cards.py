import streamlit as st


def metric_card(

    title,

    value,

    trend,

    description,

    icon,

):

    st.markdown(

        f"""

<div class="tf-card">

<h2>{icon}</h2>

<p class="metric-title">

{title}

</p>

<p class="metric-value">

{value}

</p>

<p class="metric-trend">

{trend}

</p>

<p class="description">

{description}

</p>

</div>

""",

        unsafe_allow_html=True,

    )