import streamlit as st
from utils.api_client import APIClient
from components.career_card import display_career_card

st.set_page_config(
    page_title="MindForge - Recommendations",
    page_icon="🎯",
    layout="wide"
)

st.title("Your Career Recommendations")
recommendations = [
    {
        "career_id": 1,
        "career_title": "Software Engineer",
        "match_percentage": 92.5,
        "reasoning": "Your strong analytical and technical aptitudes align perfectly with software engineering. Your problem-solving approach and interest in technology make this an excellent fit.",
        "salary_range": "$80,000 - $150,000",
        "growth_outlook": "High",
        "strengths_alignment": [
            "Analytical thinking",
            "Technical aptitude",
            "Problem-solving skills"
        ],
        "skill_gaps": [
            "Advanced algorithms",
            "System design",
            "Cloud computing"
        ],
        "next_steps": [
            "Complete a data structures course",
            "Build 2-3 portfolio projects",
            "Contribute to open source"
        ]
    },
    {
        "career_id": 2,
        "career_title": "Data Scientist",
        "match_percentage": 88.3,
        "reasoning": "Your investigative interests and mathematical aptitude make data science a strong match. You show clear potential for working with complex datasets.",
        "salary_range": "$90,000 - $160,000",
        "growth_outlook": "High",
        "strengths_alignment": [
            "Analytical mindset",
            "Mathematical reasoning",
            "Research orientation"
        ],
        "skill_gaps": [
            "Machine learning",
            "Statistical analysis",
            "Python/R programming"
        ],
        "next_steps": [
            "Learn Python and pandas",
            "Study statistics fundamentals",
            "Work on Kaggle competitions"
        ]
    }
]

st.markdown("Based on your assessment, here are your top career matches:")
for idx, rec in enumerate(recommendations, 1):
    with st.expander(f"#{idx} {rec['career_title']} - {rec['match_percentage']}% Match", expanded=(idx==1)):
        display_career_card(rec)
        st.markdown("---")
        st.markdown("###  AI Career Advisor")
        
        if st.button(f"Get Personalized Advice", key=f"advice_{idx}"):
            with st.spinner("Generating personalized guidance..."):
                # API call to AI advisor
                advice = """
                Based on your profile, software engineering is an excellent career path for you. Your analytical strengths and technical aptitude align perfectly with the core requirements of this role.

                **Why This Career Fits You:**
                - Your problem-solving approach matches how engineers think
                - Your technical interest will keep you engaged long-term
                - Your analytical skills will help you design robust systems

                **Recommended Next Steps (Start This Month):**
                1. Enroll in a comprehensive Python or JavaScript course
                2. Join coding communities like GitHub and Stack Overflow
                3. Start building a simple project (calculator, to-do app, or website)

                Remember: Every expert was once a beginner. Focus on consistent practice and you'll see rapid progress in 3-6 months.
                """
                st.info(advice)
        
        # Learning path button
        if st.button(f"View Learning Path →", key=f"path_{idx}"):
            st.session_state.selected_career = rec
            st.switch_page("Learning_Path.py")
