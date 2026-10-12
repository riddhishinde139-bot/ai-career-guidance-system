import streamlit as st

from skills import skills
from database import save_user_skills


def show_skills():

    st.title("💻 Technical Skills Assessment")

    st.write(
        "Select the technical skills that you currently know."
    )

    st.info(
        "You can select more than one skill."
    )

    # Skill selection
    selected_skills = st.multiselect(
        "Select your skills:",
        skills
    )

    if selected_skills:

        st.subheader("Skill Proficiency")

        st.write(
            "Rate your current level for each selected skill."
        )

        skill_levels = {}

        for skill in selected_skills:

            level = st.selectbox(
                f"{skill}",
                [
                    "Beginner",
                    "Intermediate",
                    "Advanced"
                ],
                key=f"level_{skill}"
            )

            skill_levels[skill] = level

        st.divider()

        if st.button(
            "Save Skills & Continue",
            type="primary",
            use_container_width=True
        ):

            save_user_skills(
                st.session_state.user_id,
                skill_levels
            )

            # Store temporarily for career matching
            st.session_state.skill_levels = skill_levels

            # Move to activities
            st.session_state.page = "activities"

            st.rerun()

    else:

        st.warning(
            "Please select at least one skill."
        )