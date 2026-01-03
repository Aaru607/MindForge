import streamlit as st
from utils.api_client import APIClient
from utils.session_manager import init_session_state
import json

st.set_page_config(
    page_title="MindForge - Assessment",
    page_icon="📝",
    layout="wide"
)

init_session_state()
api = APIClient()

st.title("📝 Career Assessment")
if 'assessment_started' not in st.session_state:
    st.session_state.assessment_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []
@st.cache_data
def load_questions():
    return [
        {
            "question_id": "q1",
            "type": "aptitude",
            "dimension": "analytical",
            "text": "You're given a complex problem with multiple variables. How do you approach it?",
            "options": [
                {"key": "A", "text": "Break it into smaller parts and analyze systematically"},
                {"key": "B", "text": "Look for creative solutions"},
                {"key": "C", "text": "Seek advice from others"},
                {"key": "D", "text": "Try different approaches"}
            ]
        },
        {
            "question_id": "q2",
            "type": "interest",
            "dimension": "investigative",
            "text": "Rate your interest in conducting research and analyzing data",
            "options": [
                {"key": "1", "text": "Not interested"},
                {"key": "2", "text": "Slightly interested"},
                {"key": "3", "text": "Moderately interested"},
                {"key": "4", "text": "Very interested"},
                {"key": "5", "text": "Extremely interested"}
            ]
        },
    ]

questions = load_questions()

if not st.session_state.assessment_started:
    st.markdown("""
    ### About This Assessment
    
    This comprehensive assessment will help us understand:
    - Your natural aptitudes and strengths
    - Your interests and preferences
    - Your skill levels across different domains
    
    **Time Required:** Approximately 15-20 minutes
    
    **Questions:** 20 carefully designed questions
    """)
    
    if st.button("Begin Assessment", type="primary"):
        st.session_state.assessment_started = True
        st.rerun()

else:
    progress = st.session_state.current_question / len(questions)
    st.progress(progress)
    st.write(f"Question {st.session_state.current_question + 1} of {len(questions)}")
    
    if st.session_state.current_question < len(questions):
        current_q = questions[st.session_state.current_question]
        
        st.markdown(f"### {current_q['text']}")
        answer = st.radio(
            "Select your answer:",
            options=[opt['key'] for opt in current_q['options']],
            format_func=lambda x: next(opt['text'] for opt in current_q['options'] if opt['key'] == x),
            key=f"q_{st.session_state.current_question}"
        )
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            if st.session_state.current_question > 0:
                if st.button("← Previous"):
                    st.session_state.current_question -= 1
                    st.rerun()
        
        with col2:
            if st.button("Next →", type="primary"):
                st.session_state.answers.append({
                    "question_id": current_q['question_id'],
                    "answer": answer,
                    "dimension": current_q['dimension'],
                    "type": current_q['type']
                })
                st.session_state.current_question += 1
                st.rerun()
    else:
        st.success("🎉 Assessment Complete!")
        st.balloons()
        
        st.markdown("""
        ### What's Next?
        
        We're now analyzing your responses to:
        - Calculate your aptitude scores
        - Identify your primary interests
        - Match you with suitable careers
        """)
        
        if st.button("View My Results", type="primary"):
            # Save assessment to backend
            with st.spinner("Analyzing your responses..."):
                # API call would go here
                import time
                time.sleep(2)
            
            st.switch_page("pages/3_🎯_Recommendations.py")
