"""
==========================================================
TalentFlow AI
Chart Components
==========================================================
"""

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ==========================================================
# HIRING FUNNEL
# ==========================================================

def hiring_funnel_chart(data):

    """
    Parameters
    ----------
    data : DataFrame

    Expected Columns
    ----------------
    application_status
    total
    """

    fig = go.Figure(

        go.Funnel(

            y=data["application_status"],

            x=data["total"],

            textinfo="value+percent initial",

            marker={

                "color": [

                    "#2563EB",
                    "#3B82F6",
                    "#60A5FA",
                    "#93C5FD",
                    "#BFDBFE",
                    "#DBEAFE",

                ]

            },

        )

    )

    fig.update_layout(

        title="Hiring Funnel",

        height=500,

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20,

        ),

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


# ==========================================================
# BAR CHART
# ==========================================================

def bar_chart(

    data,

    x,

    y,

    title,

):

    fig = px.bar(

        data,

        x=x,

        y=y,

        title=title,

        text_auto=True,

    )

    fig.update_layout(

        height=450,

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


# ==========================================================
# DONUT CHART
# ==========================================================

def donut_chart(

    data,

    names,

    values,

    title,

):

    fig = px.pie(

        data,

        names=names,

        values=values,

        hole=.65,

        title=title,

    )

    fig.update_layout(

        height=450,

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


# ==========================================================
# LINE CHART
# ==========================================================

def line_chart(

    data,

    x,

    y,

    title,

):

    fig = px.line(

        data,

        x=x,

        y=y,

        markers=True,

        title=title,

    )

    fig.update_layout(

        height=450,

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )
    
# ==========================================================
# HORIZONTAL BAR CHART
# ==========================================================

def horizontal_bar_chart(
    data,
    x,
    y,
    title,
):

    fig = px.bar(

        data,

        x=x,

        y=y,

        orientation="h",

        text_auto=True,

        title=title,

    )

    fig.update_layout(

        height=450,

        yaxis=dict(

            categoryorder="total ascending"

        ),

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


# ==========================================================
# AREA CHART
# ==========================================================

def area_chart(
    data,
    x,
    y,
    title,
):

    fig = px.area(

        data,

        x=x,

        y=y,

        title=title,

    )

    fig.update_layout(

        height=450,

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )
    
# ==========================================================
# HEATMAP
# ==========================================================

def heatmap_chart(
    data,
    x,
    y,
    z,
    title,
):

    fig = px.density_heatmap(

        data,

        x=x,

        y=y,

        z=z,

        title=title,

    )

    fig.update_layout(

        height=450,

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )