import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from dashboard.components.theme import load_theme
from dashboard.components.header import render_header
from dashboard.components.sidebar import render_sidebar

st.set_page_config(

    page_title="TalentFlow AI",

    page_icon="🤖",

    layout="wide",

    initial_sidebar_state="expanded",

)

load_theme()

render_sidebar()

render_header()

st.markdown("")

st.markdown(
"""
## Welcome

TalentFlow AI is an **AI-powered Recruitment Intelligence Platform** that combines:

- Data Engineering
- Analytics Engineering
- Artificial Intelligence
- Business Intelligence

Use the sidebar to explore each workspace.
"""
)

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        "👥 Talent Intelligence"
    )

with col2:

    st.info(
        "💼 Hiring Operations"
    )

with col3:

    st.info(
        "🤖 AI Intelligence"
    )