import streamlit as st
import time
import random as ra
import copy
import database as db

from chem_questions import CHEM_QUESTIONS
from phy_questions import PHY_QUESTIONS
from maths_questions import MATHS_QUESTIONS

# Page Setup
st.set_page_config(page_title="CBSE Class 11 Prep Hub", page_icon="🎓", layout="wide")
db.init_db()

# Real question banks (replaces the old hardcoded SAMPLE_QUESTIONS placeholder)
ALL_SUBJECTS = {
    "Chemistry": CHEM_QUESTIONS,
    "Physics": PHY_QUESTIONS,
    "Maths": MATHS_QUESTIONS,
}

OPTION_MAP = {"a": 0, "b": 1, "c": 2, "d": 3}
XP_MAP = {"Easy": 10, "Moderate": 20, "Medium": 20, "Difficult": 30}


def shuffle_question(question):
    """
    Returns a DEEP COPY of question with its options shuffled and the
    'answer' letter updated to still point at the correct option.
    Deep copy matters: the question banks are shared across every user's
    session, so shuffling in place would scramble them for everyone.
    """
    q = copy.deepcopy(question)
    correct_letter = str(q.get("answer", "a")).strip().lower()
    correct_index = OPTION_MAP.get(correct_letter, 0)
    correct_text = q["options"][correct_index]

    ra.shuffle(q["options"])

    new_index = q["options"].index(correct_text)
    letters = ["a", "b", "c", "d"]
    q["answer"] = letters[new_index]
    return q


def get_correct_text(q):
    """Resolves a question's answer letter to the actual option text."""
    letter = str(q.get("answer", "a")).strip().lower()
    return q["options"][OPTION_MAP.get(letter, 0)]


def get_explanation(q):
    return q.get("Explanation", q.get("explanation", "No explanation provided."))


def get_difficulty(q):
    return q.get("Difficulty", q.get("difficulty", "Moderate"))


# Session State Initialization
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "quiz_active" not in st.session_state:
    st.session_state.quiz_active = False
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

# --- AUTHENTICATION ---
if not st.session_state.authenticated:
    st.title("🔐 CBSE Class 11 Learning Portal")
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        login_user = st.text_input("Username", key="l_user")
        login_pass = st.text_input("Password", type="password", key="l_pass")
        if st.button("Log In"):
            if db.verify_user(login_user, login_pass):
                st.session_state.authenticated = True
                st.session_state.username = login_user
                st.success("Welcome back!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

    with tab2:
        reg_user = st.text_input("New Username", key="r_user")
        reg_pass = st.text_input("New Password", type="password", key="r_pass")
        if st.button("Create Account"):
            if reg_user and reg_pass:
                if db.register_user(reg_user, reg_pass):
                    st.success("Account created successfully! You can now log in.")
                else:
                    st.error("Username already exists.")
            else:
                st.warning("Please fill in all fields.")
    st.stop()

# --- NAVIGATION SIDEBAR ---
st.sidebar.title(f"👋 Welcome, {st.session_state.username}")
if st.sidebar.button("🚪 Log Out"):
    st.session_state.authenticated = False
    st.session_state.username = ""
    st.session_state.quiz_active = False
    st.session_state.quiz_submitted = False
    st.rerun()

page = st.sidebar.radio("Navigation", ["⚡ Timed Quiz Mode", "📚 Formula Sheets & Notes", "📊 Performance Analytics", "🏆 Leaderboard"])

# --- TIMED QUIZ COMPONENT ---
@st.fragment(run_every="1s")
def render_live_timer():
    """Renders a self-refreshing countdown timer every second."""
    if st.session_state.quiz_active and not st.session_state.quiz_submitted:
        elapsed = time.time() - st.session_state.quiz_start_time
        remaining = st.session_state.quiz_duration_sec - elapsed

        if remaining <= 0:
            st.session_state.quiz_submitted = True
            st.session_state.quiz_active = False
            st.error("⏰ Time is up! Quiz auto-submitted.")
            st.rerun()
        else:
            mins, secs = divmod(int(remaining), 60)
            if remaining < 60:
                st.error(f"⏱️ **Time Remaining:** {mins:02d}:{secs:02d}")
            else:
                st.warning(f"⏱️ **Time Remaining:** {mins:02d}:{secs:02d}")

# --- PAGE 1: TIMED QUIZ MODE ---
if page == "⚡ Timed Quiz Mode":
    st.title("⚡ Timed Quiz & Practice Mode")

    col1, col2 = st.columns(2)
    with col1:
        subject = st.selectbox("Select Subject", list(ALL_SUBJECTS.keys()))
    with col2:
        chapter = st.selectbox("Select Chapter", list(ALL_SUBJECTS[subject].keys()))

    raw_questions = ALL_SUBJECTS[subject][chapter]
    st.caption(f"📋 {len(raw_questions)} questions in this chapter")

    duration = st.slider("Select Time Limit (minutes)", min_value=1, max_value=15, value=2)

    if st.button("🚀 Start Timed Quiz") and not st.session_state.quiz_active:
        if not raw_questions:
            st.warning("No questions available for this chapter yet!")
        else:
            # Shuffle question order AND each question's options, as a deep
            # copy, so the original bank is never mutated. The shuffled set
            # is stored once here and reused for both the form and grading,
            # so what the student sees and what gets graded always match.
            shuffled = [shuffle_question(q) for q in raw_questions]
            ra.shuffle(shuffled)

            st.session_state.quiz_active = True
            st.session_state.quiz_submitted = False
            st.session_state.quiz_start_time = time.time()
            st.session_state.quiz_duration_sec = duration * 60
            st.session_state.user_answers = {}
            st.session_state.quiz_questions = shuffled
            st.session_state.quiz_subject = subject
            st.session_state.quiz_chapter = chapter
            st.rerun()

    if st.session_state.quiz_active:
        render_live_timer()
        questions = st.session_state.quiz_questions

        with st.form("quiz_form"):
            for idx, q in enumerate(questions):
                st.write(f"**Q{idx + 1}: {q['question']}**")
                st.session_state.user_answers[idx] = st.radio(
                    f"Select answer for Q{idx + 1}:",
                    q["options"],
                    key=f"q_{idx}",
                    index=None
                )
                st.write("---")

            submitted = st.form_submit_button("Submit Answers")
            if submitted:
                st.session_state.quiz_submitted = True
                st.session_state.quiz_active = False
                st.rerun()

    if st.session_state.quiz_submitted:
        st.subheader("📝 Quiz Results")
        # Use the SAME shuffled question set the student was actually shown -
        # re-fetching fresh from ALL_SUBJECTS here would grade against a
        # different (unshuffled, re-randomized) version than what was displayed.
        questions = st.session_state.quiz_questions
        quiz_subject = st.session_state.quiz_subject
        quiz_chapter = st.session_state.quiz_chapter
        correct_count = 0
        total_xp = 0

        for idx, q in enumerate(questions):
            user_ans = st.session_state.user_answers.get(idx)
            correct_text = get_correct_text(q)
            is_correct = (user_ans == correct_text)
            xp = XP_MAP.get(get_difficulty(q), 20) if is_correct else 0
            total_xp += xp

            # Save progress directly to database
            db.update_user_stats(st.session_state.username, xp, is_correct, quiz_subject, quiz_chapter)

            if is_correct:
                correct_count += 1
                st.success(f"**Q{idx + 1}: Correct!** (+{xp} XP)")
            else:
                shown = user_ans if user_ans is not None else "(no answer selected)"
                st.error(f"**Q{idx + 1}: Incorrect.** Your answer: {shown} | Correct Answer: {correct_text}")
            st.caption(f"💡 Explanation: {get_explanation(q)}")

        st.info(f"Final Score: **{correct_count} / {len(questions)}**  |  **+{total_xp} XP earned**")
        if st.button("Take Another Quiz"):
            st.session_state.quiz_submitted = False
            st.rerun()

# --- PAGE 2: FORMULA SHEETS & NOTES ---
elif page == "📚 Formula Sheets & Notes":
    st.title("📚 Formula Sheets & Quick Revision")

    selected_sub = st.selectbox("Select Subject", ["Chemistry", "Physics", "Maths"])

    if selected_sub == "Chemistry":
        with st.expander("🧪 Some Basic Concepts of Chemistry"):
            st.markdown("""
            - **Mole Concept:** $n = \\frac{\\text{Mass}}{\\text{Molar Mass}} = \\frac{N}{N_A}$
            - **Molarity (M):** $M = \\frac{\\text{Moles of Solute}}{\\text{Volume of Solution (L)}}$
            - **Molality (m):** $m = \\frac{\\text{Moles of Solute}}{\\text{Mass of Solvent (kg)}}$
            """)
        with st.expander("⚛️ Structure of Atom"):
            st.markdown("""
            - **de Broglie Wavelength:** $\\lambda = \\frac{h}{p} = \\frac{h}{mv}$
            - **Heisenberg Uncertainty Principle:** $\\Delta x \\cdot \\Delta p \\ge \\frac{h}{4\\pi}$
            """)

    elif selected_sub == "Physics":
        with st.expander("📐 Units and Measurements"):
            st.markdown("""
            - **Percentage Error:** $\\frac{\\Delta A}{A} \\times 100\\%$
            - **Combination of Errors:** $\\frac{\\Delta Z}{Z} = \\frac{\\Delta A}{A} + \\frac{\\Delta B}{B}$
            """)

    elif selected_sub == "Maths":
        with st.expander("🔢 Sets, Relations and Functions"):
            st.markdown("""
            - **Number of subsets of a set with n elements:** $2^n$
            - **n(A ∪ B):** $n(A) + n(B) - n(A \\cap B)$
            """)
        with st.expander("📈 Permutations & Combinations"):
            st.markdown("""
            - **Permutations:** $^nP_r = \\frac{n!}{(n-r)!}$
            - **Combinations:** $^nC_r = \\frac{n!}{r!(n-r)!}$
            """)
        with st.expander("📐 Trigonometric Identities"):
            st.markdown("""
            - $\\sin^2\\theta + \\cos^2\\theta = 1$
            - $1 + \\tan^2\\theta = \\sec^2\\theta$
            """)

# --- PAGE 3: PERFORMANCE ANALYTICS ---
elif page == "📊 Performance Analytics":
    st.title("📊 Your Performance & Weak Area Analytics")
    analytics = db.get_user_chapter_analytics(st.session_state.username)

    if analytics:
        st.dataframe(analytics, use_container_width=True)

        # Highlight weak areas
        weak_areas = [item for item in analytics if item["accuracy"] < 60.0]
        if weak_areas:
            st.warning("⚠️ **Focus Areas Recommended for Revision:**")
            for item in weak_areas:
                st.write(f"- **{item['subject']}**: {item['chapter']} (Accuracy: {item['accuracy']}%)")
        else:
            st.balloons()
            st.success("🎉 Great job! Your accuracy across all attempted chapters is above 60%.")
    else:
        st.info("No quiz data available yet. Complete a timed quiz to generate performance analytics!")

# --- PAGE 4: LEADERBOARD ---
elif page == "🏆 Leaderboard":
    st.title("🏆 Student Leaderboard")
    leaderboard_data = db.get_leaderboard()
    if leaderboard_data:
        st.dataframe(leaderboard_data, use_container_width=True)
    else:
        st.info("Leaderboard is currently empty.")