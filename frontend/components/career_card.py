import streamlit as st

def display_career_card(recommendation: dict):
    """Display a formatted career recommendation card"""
    
    # Match percentage with color
    match = recommendation['match_percentage']
    if match >= 90:
        color = "green"
    elif match >= 75:
        color = "blue"
    else:
        color = "orange"
    
    st.markdown(f"### Match Score: :{color}[{match}%]")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**Why This Career Fits You:**")
        st.write(recommendation['reasoning'])
        
        st.markdown("**Your Strengths Aligned:**")
        for strength in recommendation['strengths_alignment']:
            st.markdown(f" {strength}")
    
    with col2:
        st.metric("Salary Range", recommendation['salary_range'])
        st.metric("Growth Outlook", recommendation['growth_outlook'])
    
    # Skill gaps
    if recommendation.get('skill_gaps'):
        with st.expander("Skills to Develop"):
            for gap in recommendation['skill_gaps']:
                st.markdown(f"- {gap}")
    
    # Next steps
    if recommendation.get('next_steps'):
        with st.expander(" Recommended Next Steps"):
            for idx, step in enumerate(recommendation['next_steps'], 1):
                st.markdown(f"{idx}. {step}")
