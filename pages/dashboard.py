import streamlit as st


def show_dashboard():

    st.title(
        f"Welcome, {st.session_state.user_name}! 👋"
    )

    st.write(
        "Welcome to your AI Career Guidance dashboard."
    )

    st.divider()

    st.subheader("What would you like to do?")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🎯 Start Assessment",
            use_container_width=True
        ):

            st.session_state.page = "riasec"
            st.rerun()

    with col2:

        if st.button(
            "👤 My Profile",
            use_container_width=True
        ):

            st.session_state.page = "profile"
            st.rerun()

    st.divider()

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.user_name = None
        st.session_state.page = "dashboard"

        st.rerun()