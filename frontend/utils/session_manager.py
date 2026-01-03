import streamlit as st

def init_session_state():
    """Initialize session state variables"""
    
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
    
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if 'assessment_complete' not in st.session_state:
        st.session_state.assessment_complete = False
    
    if 'recommendations' not in st.session_state:
        st.session_state.recommendations = []
    
    if 'selected_career' not in st.session_state:
        st.session_state.selected_career = None

def clear_session():
    """Clear all session data"""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
