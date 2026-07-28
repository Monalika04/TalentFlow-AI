from datetime import datetime

import streamlit as st


def render_header(
    page_title: str,
    page_description: str,
):
    """
    Render the standard TalentFlow AI header.
    """

    left, right = st.columns([7, 3])

    with left:

        st.markdown(
            f"""
### 🤖 TalentFlow AI

#### {page_title}

{page_description}
"""
        )

        st.caption(
            f"Last Updated • {datetime.now().strftime('%d %b %Y %I:%M %p')}"
        )

    with right:

        st.text_input(
            label="Search",
            placeholder="Search candidates, jobs...",
            key="global_search",
        )

        btn1, btn2, btn3 = st.columns(3)

        with btn1:
            st.button(
                "🔄",
                use_container_width=True,
                help="Refresh Dashboard",
            )

        with btn2:
            st.button(
                "🔔",
                use_container_width=True,
                help="Notifications",
            )

        with btn3:
            st.button(
                "👤",
                use_container_width=True,
                help="Profile",
            )

    st.divider()