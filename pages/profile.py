import streamlit as st

from database import (
    get_riasec_result,
    get_user_skills,
    get_user_activities
)


def show_profile():

    st.title("👤 My Profile")

    st.write(
        f"Welcome, **{st.session_state.user_name}**!"
    )

    st.divider()

    # -----------------------------------------
    # RIASEC PROFILE
    # -----------------------------------------

    st.header("🎯 RIASEC Profile")

    riasec_result = get_riasec_result(
        st.session_state.user_id
    )

    if riasec_result:

        R, I, A, S, E, C, status = riasec_result

        riasec_scores = {
            "Realistic": R,
            "Investigative": I,
            "Artistic": A,
            "Social": S,
            "Enterprising": E,
            "Conventional": C
        }

        # Display scores

        for category, score in riasec_scores.items():

            st.write(
                f"**{category}:** {score}/20"
            )

            st.progress(score / 20)

        # Find strongest areas

        strongest = sorted(
            riasec_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        st.subheader("🌟 Strongest Areas")

        for i, (category, score) in enumerate(
            strongest[:3],
            start=1
        ):

            st.write(
                f"{i}. **{category}** — {score}/20"
            )

    else:

        st.info(
            "You have not completed the RIASEC assessment yet."
        )

    st.divider()

    # -----------------------------------------
    # TECHNICAL SKILLS
    # -----------------------------------------

    st.header("💻 Technical Skills")

    user_skills = get_user_skills(
        st.session_state.user_id
    )

    if user_skills:

        for skill, level in user_skills:

            st.write(
                f"✓ **{skill}** — {level}"
            )

    else:

        st.info(
            "No technical skills have been added yet."
        )

    st.divider()

    # -----------------------------------------
    # WORK ACTIVITIES
    # -----------------------------------------

    st.header("🛠️ Work Activities")

    user_activities = get_user_activities(
        st.session_state.user_id
    )

    if user_activities:

        for activity in user_activities:

            st.write(
                f"✓ {activity}"
            )

    else:

        st.info(
            "No work activities have been selected yet."
        )

    st.divider()

    # -----------------------------------------
    # BACK TO DASHBOARD
    # -----------------------------------------

    if st.button(
        "🏠 Back to Dashboard",
        use_container_width=True
    ):

        st.session_state.page = "dashboard"

        st.rerun()