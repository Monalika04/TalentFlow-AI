from pathlib import Path

import plotly.io as pio
import streamlit as st


# ==========================================================
# LOAD CSS
# ==========================================================

def load_theme():

    css_path = (
        Path(__file__)
        .parent.parent
        / "assets"
        / "theme.css"
    )

    with open(
        css_path,
        encoding="utf-8",
    ) as css:

        st.markdown(

            f"<style>{css.read()}</style>",

            unsafe_allow_html=True,

        )

    configure_plotly()


# ==========================================================
# PLOTLY TEMPLATE
# ==========================================================

def configure_plotly():

    template = {

        "layout": {

            "paper_bgcolor": "#0F172A",

            "plot_bgcolor": "#1E293B",

            "font": {

                "family": "Segoe UI",

                "size": 13,

                "color": "#F8FAFC",

            },

            "colorway": [

                "#2563EB",
                "#22C55E",
                "#F59E0B",
                "#EF4444",
                "#8B5CF6",
                "#06B6D4",

            ],

            "xaxis": {

                "showgrid": False,

                "zeroline": False,

                "linecolor": "#334155",

                "tickcolor": "#94A3B8",

            },

            "yaxis": {

                "gridcolor": "#334155",

                "zeroline": False,

                "linecolor": "#334155",

                "tickcolor": "#94A3B8",

            },

            "legend": {

                "bgcolor": "rgba(0,0,0,0)",

                "font": {

                    "color": "#F8FAFC",

                },

            },

            "margin": {

                "l": 25,

                "r": 25,

                "t": 40,

                "b": 25,

            },

        }

    }

    pio.templates["talentflow"] = template

    pio.templates.default = "talentflow"


# ==========================================================
# PAGE CONFIG
# ==========================================================

def configure_page(

    title: str,

):

    st.set_page_config(

        page_title=title,

        page_icon="🤖",

        layout="wide",

        initial_sidebar_state="expanded",

    )