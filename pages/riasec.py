import streamlit as st

from questions import questions
from database import save_riasec_result


category_names = {
    "R": "Realistic",
    "I": "Investigative",
    "A": "Artistic",
    "S": "Social",
    "E": "Enterprising",
    "C": "Conventional"
}


category_descriptions = {
    "R": "You prefer practical, hands-on and technical activities.",
    "I": "You enjoy analysis, problem-solving and understanding how things work.",
    "A": "You enjoy creativity, design and coming up with new ideas.",
    "S": "You enjoy helping, teaching and working with other people.",
    "E": "You enjoy leadership, taking initiative and making decisions.",
    "C": "You prefer organization, structure, accuracy and clear processes."
}


def show_riasec():

    st.title("🎯 RIASEC Career Assessment")

    st.write(
        "Answer each question based on how much "
        "you agree with the statement."
    )

    st.info(
        "1 = Strongly Disagree | "
        "2 = Disagree | "
        "3 = Neutral | "
        "4 = Agree | "
        "5 = Strongly Agree"
    )

    st.divider()

    answers = {}
    question_number = 1

    for category, question_list in questions.items():

        st.subheader(category_names[category])

        for question in question_list:

            answer = st.radio(
                question,
                [1, 2, 3, 4, 5],

                format_func=lambda x: {
                    1: "1 - Strongly Disagree",
                    2: "2 - Disagree",
                    3: "3 - Neutral",
                    4: "4 - Agree",
                    5: "5 - Strongly Agree"
                }[x],

                key=f"question_{question_number}"
            )

            answers[question_number] = (
                category,
                answer
            )

            question_number += 1

    st.divider()

    if st.button(
        "Submit RIASEC Assessment",
        type="primary",
        use_container_width=True
    ):

        scores = {
            "R": 0,
            "I": 0,
            "A": 0,
            "S": 0,
            "E": 0,
            "C": 0
        }

        for category, answer in answers.values():
            scores[category] += answer

        save_riasec_result(
            st.session_state.user_id,
            scores,
            "completed"
        )

        st.session_state.riasec_scores = scores

        st.session_state.page = "riasec_result"

        st.rerun()


def show_riasec_result():

    st.title("🎯 Your RIASEC Profile")

    scores = st.session_state.riasec_scores

    sorted_scores = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    st.subheader("Your RIASEC Scores")

    for category, score in sorted_scores:

        st.write(
            f"**{category_names[category]}:** "
            f"{score}/20"
        )

        st.progress(score / 20)

    st.divider()

    st.subheader("🌟 Your Strongest Areas")

    for i, (category, score) in enumerate(
        sorted_scores[:3],
        start=1
    ):

        st.markdown(
            f"### {i}. "
            f"{category_names[category]} — {score}/20"
        )

        st.write(
            category_descriptions[category]
        )

    st.divider()

    st.success(
        "Your RIASEC assessment has been saved successfully!"
    )

    if st.button(
        "➡️ Continue to Detailed Assessment",
        type="primary",
        use_container_width=True
    ):

        st.session_state.page = "skills"

        st.rerun()