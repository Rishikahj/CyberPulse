import streamlit as st

st.set_page_config(page_title="CyberPulse – Cyber Hygiene Checker", layout="centered")
st.title("🛡️ CyberPulse – Smart Cyber Hygiene Checker")

page = st.sidebar.radio("Navigate", ["Take Quiz", "View Result", "Suggestions", "Password Strength Checker"])

if "answers" not in st.session_state:
    st.session_state.answers = []
if "score" not in st.session_state:
    st.session_state.score = 0

questions = [
    "Do you use strong, unique passwords for each account?",
    "Do you use two-factor authentication whenever possible?",
    "Do you regularly update your software and apps?",
    "Do you avoid clicking on unknown email links?",
    "Do you use a VPN when on public Wi-Fi?",
    "Do you have antivirus or endpoint protection?",
    "Do you back up your data regularly?",
    "Do you avoid reusing passwords across platforms?",
    "Do you check app permissions before allowing them?",
    "Do you limit personal info shared on social media?"
]

if page == "Take Quiz":
    st.subheader("📝 Cyber Hygiene Quiz")
    st.session_state.answers = []
    st.session_state.score = 0
    for i, q in enumerate(questions):
        ans = st.radio(q, ["Yes", "No"], key=f"q{i}")
        st.session_state.answers.append(ans)
        if ans == "Yes":
            st.session_state.score += 10
    if st.button("Submit Quiz"):
        st.success("Submitted! Go to 'View Result' tab.")

elif page == "View Result":
    st.subheader("📊 Result")
    score = st.session_state.score
    st.info(f"Your Score: **{score}/100**")
    if score >= 80:
        st.success("Excellent Cyber Hygiene!")
    elif score >= 50:
        st.warning("Moderate Hygiene – Needs Improvement.")
    else:
        st.error("Poor Hygiene – Review suggestions.")

elif page == "Suggestions":
    st.subheader("💡 Tips for Better Cyber Hygiene")
    weak_points = [questions[i] for i, ans in enumerate(st.session_state.answers) if ans == "No"]
    if weak_points:
        for i, q in enumerate(weak_points):
            st.markdown(f"**{i+1}. {q}**")
            st.caption("👉 Improve this practice for better safety.")
    else:
        st.success("You're doing great! Keep it up.")

elif page == "Password Strength Checker":
    st.subheader("🔐 Password Strength Checker")
    pw = st.text_input("Enter a sample password")

    def evaluate_password(pw):
        import re
        score = 0
        if len(pw) >= 8: score += 1
        if re.search(r"[A-Z]", pw): score += 1
        if re.search(r"[a-z]", pw): score += 1
        if re.search(r"[0-9]", pw): score += 1
        if re.search(r"[@$!%*?&]", pw): score += 1
        return score

    if pw:
        strength = evaluate_password(pw)
        if strength <= 2:
            st.error("Weak Password")
        elif strength == 3:
            st.warning("Moderate Password")
        else:
            st.success("Strong Password")
