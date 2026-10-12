import streamlit as st

from careers import (
    careers,
    career_skills,
    career_activities
)

from matching import rank_careers


def show_career_results():

    st.title("🎯 Your Career Matches")

    st.write(
        "Based on your interests, skills and preferred "
        "activities, these are your top career matches."
    )

    # Get user's RIASEC scores
    riasec_scores = st.session_state.riasec_scores

    # Get user's skill levels
    user_skill_levels = st.session_state.skill_levels

    # Get user's activities
    user_activities = st.session_state.user_activities

    # Calculate career rankings
    results = rank_careers(
        riasec_scores,
        user_skill_levels,
        user_activities,
        careers,
        career_skills,
        career_activities
    )

    st.divider()

    # Display top 3 careers
    for i, result in enumerate(
        results[:3],
        start=1
    ):

        st.subheader(
            f"{i}. {result['career']}"
        )

        st.metric(
            "Overall Match",
            f"{result['final']}%"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "RIASEC Match",
                f"{result['riasec']}%"
            )

        with col2:

            st.metric(
                "Skill Match",
                f"{result['skills']}%"
            )

        with col3:

            st.metric(
                "Activity Match",
                f"{result['activities']}%"
            )

        st.divider()