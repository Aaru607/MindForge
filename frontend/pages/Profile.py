import streamlit as st

st.set_page_config(
    page_title="MindForge - Profile",
    page_icon="👤",
    layout="wide"
)

st.title("My Profile")

tab1, tab2, tab3 = st.tabs(["Personal Info", "Assessment History", "Saved Careers"])

with tab1:
    st.markdown("### Personal Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name", value="John Doe")
        email = st.text_input("Email", value="john@example.com")
        age = st.number_input("Age", min_value=13, max_value=100, value=22)
    
    with col2:
        education = st.selectbox(
            "Education Level",
            ["High School", "Diploma", "Undergraduate", "Graduate", "Postgraduate"]
        )
        location = st.text_input("Location", value="New York, USA")
    
    if st.button("Update Profile", type="primary"):
        st.success("Profile updated successfully!")

with tab2:
    st.markdown("### Assessment History")
    
    # Mock assessment history
    assessments = [
        {"date": "2024-01-15", "type": "Full Assessment", "status": "Completed"},
        {"date": "2023-12-10", "type": "Skills Update", "status": "Completed"}
    ]
    
    for assessment in assessments:
        with st.expander(f"{assessment['date']} - {assessment['type']}"):
            st.write(f"Status: {assessment['status']}")
            if st.button("View Results", key=assessment['date']):
                st.info("Results will be displayed here")

with tab3:
    st.markdown("### Saved Careers")
    
    st.info("Careers you've saved for future reference")
    
    saved_careers = [
        {"title": "Software Engineer", "match": "92%"},
        {"title": "Data Scientist", "match": "88%"}
    ]
    
    for career in saved_careers:
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"**{career['title']}**")
        with col2:
            st.write(career['match'])
        with col3:
            if st.button("View", key=career['title']):
                st.info(f"Details for {career['title']}")
