import streamlit as st
from utils.session_manager import init_session_state

st.set_page_config(
    page_title="MindForge - Home",
    page_icon="🏠",
    layout="wide"
)

init_session_state()

st.title("Welcome to MindForge")
st.markdown("### Your AI-Powered Career Intelligence Platform")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    MindForge helps you make informed career decisions through:
    
    - **📊 Comprehensive Assessment**: Evaluate your aptitudes, interests, and skills
    - **🎯 AI-Powered Recommendations**: Get personalized career matches
    - **📚 Learning Roadmaps**: Structured paths to achieve your career goals
    - **💡 Expert Guidance**: AI-driven insights and actionable advice
    """)
    
    if st.button(" Start Your Journey", type="primary", use_container_width=True):
        st.switch_page("Assessment.py")

with col2:
    st.info("**For Students & Professionals**\n\nWhether you're exploring options or planning a career transition, MindForge provides data-driven guidance.")

st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Career Paths", "500+", delta="Growing")
with col2:
    st.metric("Skills Mapped", "2000+", delta="Updated")
with col3:
    st.metric("Users Helped", "10K+", delta="This month")
with col4:
    st.metric("Success Rate", "92%", delta="User satisfaction")
st.markdown("## 🔄 How It Works")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 1️⃣ Take Assessment")
    st.write("Complete our comprehensive assessment covering aptitudes, interests, and skills")

with col2:
    st.markdown("### 2️⃣ Get Recommendations")
    st.write("Receive AI-powered career matches with detailed explanations")

with col3:
    st.markdown("### 3️⃣ Follow Your Path")
    st.write("Access personalized learning roadmaps to achieve your goals")
