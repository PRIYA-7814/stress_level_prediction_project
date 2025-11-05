import streamlit as st
import numpy as np

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Student Stress Level Predictor",
    page_icon="🧠",
    layout="centered"
)

# ---------- CUSTOM STYLING ----------
st.markdown("""
    <style>
    /* --- Global background --- */
    body, .stApp {
        background: linear-gradient(135deg, #0f0f0f, #1a1a1a, #222831);
        color: #00ff9d;
        font-family: 'Fira Code', monospace;
    }

    /* --- Headings --- */
    h1, h2, h3, h4 {
        color: #00ff9d;
        text-shadow: 0 0 15px #00ffaa;
    }

    /* --- Buttons --- */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00ffaa, #00b3ff);
        color: black;
        border-radius: 10px;
        font-weight: bold;
        box-shadow: 0 0 10px #00ffaa;
        transition: 0.3s;
    }

    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #ff00c8, #00b3ff);
        color: white;
        transform: scale(1.05);
    }

    /* --- Input boxes --- */
    .stTextInput>div>div>input {
        background-color: #161616;
        color: #00ff9d;
        border: 1px solid #00ffaa;
    }

    /* --- Center elements --- */
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    /* --- Sidebar --- */
    .css-1d391kg, .css-1lcbmhc {
        background-color: #1a1a1a !important;
    }
    </style>
""", unsafe_allow_html=True)


# ---------- DEFAULT LOGIN CREDENTIALS ----------
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "1234"

# ---------- LOGIN PAGE ----------
def login_page():
    st.title("🔐 Login Page")
    st.write("Please log in to access the Student Stress Level Predictor.")
    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):
        if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
            st.session_state.logged_in = True
            st.success("✅ Login successful! Redirecting...")
            st.rerun()
        else:
            st.error("❌ Invalid username or password.")

# ---------- USER TYPE SELECTION ----------
def user_selection_page():
    st.title("🎯 Choose Student Type")
    st.write("Select the type of student for stress prediction:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏫 School Student"):
            st.session_state.user_type = "school"
            st.rerun()
    with col2:
        if st.button("🎓 College Student"):
            st.session_state.user_type = "college"
            st.rerun()

# ---------- SCHOOL STRESS PREDICTOR ----------
def school_predictor():
    st.subheader("🏫 School Student Stress Level Predictor")

    st.write("Fill in the details below:")
    study_hours = st.slider("📘 Study hours per day", 0, 12, 5)
    sleep_hours = st.slider("💤 Sleep hours per day", 0, 12, 7)
    homework_load = st.selectbox("📚 Homework Load", ["Low", "Medium", "High"])

    extracurricular_hours = st.slider("⚽ Extracurricular activity hours", 0, 6, 2)
    screen_time = st.slider("📱 Screen time (hours per day)", 0, 12, 4)
    parental_pressure = st.slider("👨‍👩‍👧‍👦 Parental pressure level", 0, 10, 5)
    test_anxiety = st.slider("📉 Exam/Test anxiety level", 0, 10, 4)
    social_activity = st.slider("🤝 Social interaction per week (hours)", 0, 20, 8)

    if st.button("🔍 Predict Stress Level"):
        stress_score = (
            (study_hours * 2 - sleep_hours)
            + (3 if homework_load == "High" else 2 if homework_load == "Medium" else 1)
            + extracurricular_hours * 0.5
            + screen_time * 0.3
            + parental_pressure * 0.4
            + test_anxiety * 0.6
            - social_activity * 0.2
        )

        if stress_score < 15:
            st.success("😌 Low Stress Level — Keep it up!")
        elif stress_score < 25:
            st.warning("😟 Moderate Stress Level — Take breaks often!")
        else:
            st.error("😫 High Stress Level — You may need rest or support!")

# ---------- COLLEGE STRESS PREDICTOR ----------
def college_predictor():
    st.subheader("🎓 College Student Stress Level Predictor")

    st.write("Fill in the details below:")
    cgpa = st.slider("📊 Current CGPA", 0.0, 10.0, 7.5)
    assignments = st.selectbox("📝 Assignment Workload", ["Low", "Medium", "High"])
    part_time_job = st.radio("💼 Do you have a part-time job?", ["Yes", "No"])

    sleep_hours = st.slider("💤 Sleep hours per day", 0, 12, 6)
    study_hours = st.slider("📘 Study hours per day", 0, 12, 5)
    social_life = st.slider("🎉 Social life (hours per week)", 0, 30, 10)
    financial_stress = st.slider("💰 Financial stress level", 0, 10, 5)
    internship_load = st.slider("🧑‍💼 Internship workload (hours/week)", 0, 40, 10)

    if st.button("🔍 Predict Stress Level"):
        stress_score = (
            (10 - cgpa)
            + (3 if assignments == "High" else 2 if assignments == "Medium" else 1)
            + (2 if part_time_job == "Yes" else 0)
            + (12 - sleep_hours) * 0.5
            + study_hours * 0.5
            + financial_stress * 0.6
            + internship_load * 0.4
            - social_life * 0.2
        )

        if stress_score < 15:
            st.success("😎 Low Stress — You're balancing things well!")
        elif stress_score < 25:
            st.warning("😐 Moderate Stress — Manage your schedule carefully.")
        else:
            st.error("🔥 High Stress — Prioritize mental health and rest!")

# ---------- MAIN PAGE ----------
def main_page():
    if st.session_state.user_type == "school":
        school_predictor()
    elif st.session_state.user_type == "college":
        college_predictor()

    if st.button("🔙 Back"):
        del st.session_state.user_type
        st.rerun()

# ---------- APP CONTROLLER ----------
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_type" not in st.session_state:
        st.session_state.user_type = None

    if not st.session_state.logged_in:
        login_page()
    elif st.session_state.user_type is None:
        user_selection_page()
    else:
        main_page()

if __name__ == "__main__":
    main()
