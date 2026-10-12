import streamlit as st

from database import register_user, login_user


def show_login():

    st.title("🎯 AI Career Guidance System")

    st.write(
        "Discover career options based on your "
        "interests and technical skills."
    )

    st.divider()

    option = st.radio(
        "Choose an option",
        ["Login", "Create Account"],
        horizontal=True
    )

    # -----------------------------------------
    # LOGIN
    # -----------------------------------------

    if option == "Login":

        st.subheader("Welcome Back!")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login", type="primary"):

            if username == "" or password == "":
                st.warning(
                    "Please enter username and password."
                )

            else:

                user = login_user(
                    username,
                    password
                )

                if user:

                    st.session_state.logged_in = True
                    st.session_state.user_id = user[0]
                    st.session_state.user_name = user[1]
                    st.session_state.page = "dashboard"

                    st.success("Login successful!")

                    st.rerun()

                else:

                    st.error(
                        "Invalid username or password."
                    )

    # -----------------------------------------
    # REGISTER
    # -----------------------------------------

    else:

        st.subheader("Create Your Account")

        name = st.text_input("Full Name")

        username = st.text_input("Choose Username")

        password = st.text_input(
            "Create Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button(
            "Create Account",
            type="primary"
        ):

            if (
                name == ""
                or username == ""
                or password == ""
                or confirm_password == ""
            ):

                st.warning(
                    "Please fill all the fields."
                )

            elif password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            else:

                success = register_user(
                    name,
                    username,
                    password
                )

                if success:

                    st.success(
                        "Account created successfully! "
                        "You can now login."
                    )

                else:

                    st.error(
                        "Username already exists."
                    )