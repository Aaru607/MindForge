import streamlit as st

st.set_page_config(
    page_title="MindForge - Learning Path",
    page_icon="📚",
    layout="wide"
)

st.title(" Your Learning Roadmap")

if 'selected_career' not in st.session_state:
    st.warning("Please select a career from recommendations first")
    if st.button("Go to Recommendations"):
        st.switch_page("Recommendations.py")
else:
    career = st.session_state.selected_career
    
    st.markdown(f"## Path to becoming a {career['career_title']}")
    
    # Timeline view
    st.markdown("### 6-Month Learning Timeline")
    
    phases = [
        {
            "name": "Phase 1: Foundation (Months 1-2)",
            "focus": "Building core skills",
            "skills": ["Programming Basics", "Data Structures"],
            "resources": [
                {"name": "Python for Beginners", "type": "Course", "duration": "4 weeks", "platform": "Coursera"},
                {"name": "Build a Calculator App", "type": "Project", "duration": "1 week", "platform": "Self-paced"}
            ],
            "milestones": [
                "Complete 20 coding exercises",
                "Build first project",
                "Understand basic algorithms"
            ]
        },
        {
            "name": "Phase 2: Intermediate (Months 3-4)",
            "focus": "Deepening technical knowledge",
            "skills": ["Algorithms", "System Design"],
            "resources": [
                {"name": "Algorithms Specialization", "type": "Course", "duration": "6 weeks", "platform": "Coursera"},
                {"name": "Build a Todo App with Database", "type": "Project", "duration": "2 weeks", "platform": "Self-paced"}
            ],
            "milestones": [
                "Solve 50 LeetCode problems",
                "Understand design patterns",
                "Deploy a web application"
            ]
        },
        {
            "name": "Phase 3: Advanced (Months 5-6)",
            "focus": "Portfolio & specialization",
            "skills": ["Cloud Computing", "Advanced Topics"],
            "resources": [
                {"name": "AWS Certified Developer", "type": "Certification", "duration": "8 weeks", "platform": "AWS"},
                {"name": "Full-Stack Portfolio Project", "type": "Project", "duration": "4 weeks", "platform": "Self-paced"}
            ],
            "milestones": [
                "Complete capstone project",
                "Earn industry certification",
                "Create professional portfolio"
            ]
        }
    ]
    
    for idx, phase in enumerate(phases, 1):
        with st.expander(phase['name'], expanded=(idx==1)):
            st.markdown(f"**Focus:** {phase['focus']}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Skills to Learn:**")
                for skill in phase['skills']:
                    st.markdown(f"- {skill}")
            
            with col2:
                st.markdown("**Milestones:**")
                for milestone in phase['milestones']:
                    st.checkbox(milestone, key=f"milestone_{idx}_{milestone}")
            
            st.markdown("**Recommended Resources:**")
            for resource in phase['resources']:
                st.info(f"**{resource['name']}** ({resource['type']})\n\n"
                       f"Platform: {resource['platform']} | Duration: {resource['duration']}")
    
    # Additional resources
    st.markdown("---")
    st.markdown("### Additional Opportunities")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Certifications:**")
        st.markdown("- AWS Certified Developer")
        st.markdown("- Google Cloud Professional")
        st.markdown("- Microsoft Azure Developer")
    
    with col2:
        st.markdown("**Networking:**")
        st.markdown("- Join LinkedIn tech groups")
        st.markdown("- Attend local meetups")
        st.markdown("- Contribute to open source")
