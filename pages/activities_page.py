import streamlit as st

from activities import activities
from database import save_user_activities


def show_activities():

    st.title("🛠️ Work Activities")

    st.write(
        "Select the activities that you enjoy or "
        "would like to do in your career."
    )

    st.info(
        "Choose the activities that interest you. "
        "You can select more than one."
    )

    selected_activities = st.multiselect(
        "Select activities:",
        activities
    )

    st.divider()

    if st.button(
        "Save Activities & See Career Matches",
        type="primary",
        use_container_width=True
    ):

        if len(selected_activities) == 0:

            st.warning(
                "Please select at least one activity."
            )

        else:

            save_user_activities(
                st.session_state.user_id,
                selected_activities
            )

            # Store for career matching
            st.session_state.user_activities = (
                selected_activities
            )

            # Move to career results
            st.session_state.page = "career_results"

            st.rerun()