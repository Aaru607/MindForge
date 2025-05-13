import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import numpy as np

# Page configuration
st.set_page_config(
    page_title="MindForge - Career Guidance Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for page navigation if not exists
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stat-box {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #1E1E1E;
    }
    .highlight {
        background: linear-gradient(120deg, #FF4B4B20 0%, #FF4B4B20 100%);
        background-repeat: no-repeat;
        background-size: 100% 0.4em;
        background-position: 0 88%;
        transition: background-size 0.25s ease-in;
    }
    .highlight:hover {
        background-size: 100% 100%;
    }
    .feature-card {
        border: 1px solid #f0f0f0;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        background: white;
        transition: all 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    
    /* New Sidebar Styles */
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    
    .sidebar-title {
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 1rem;
        border-bottom: 2px solid #FF4B4B20;
    }
    
    .nav-link {
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        background-color: white;
        transition: all 0.3s ease;
        text-decoration: none;
        color: #1E1E1E;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .nav-link:hover {
        background-color: #FF4B4B10;
        transform: translateX(5px);
    }
    
    .nav-link.active {
        background-color: #FF4B4B;
        color: white;
    }
    
    .sidebar-footer {
        position: fixed;
        bottom: 0;
        padding: 1rem;
        width: 100%;
        background-color: #f8f9fa;
        border-top: 1px solid #FF4B4B20;
        text-align: center;
    }
    
    .profile-section {
        text-align: center;
        padding: 1rem;
        margin-bottom: 2rem;
    }
    
    .profile-image {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        margin: 0 auto;
        border: 3px solid #FF4B4B;
        padding: 3px;
    }
    
    .progress-ring {
        margin: 1rem auto;
        position: relative;
        width: 120px;
        height: 120px;
    }
    
    .notification-badge {
        background-color: #FF4B4B;
        color: white;
        border-radius: 50%;
        padding: 0.25rem 0.5rem;
        font-size: 0.8rem;
        position: absolute;
        top: -5px;
        right: -5px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Profile Section
    st.markdown("""
        <div class='profile-section'>
            <img src='https://img.freepik.com/free-vector/businessman-character-avatar-isolated_24877-60111.jpg' 
                 class='profile-image'>
            <h3 style='margin-top: 1rem;'>Welcome Back!</h3>
            <p style='color: #666;'>Your Career Journey Awaits</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Progress Ring
    st.markdown("""
        <div class='progress-ring'>
            <div style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);'>
                <h4 style='color: #FF4B4B; margin: 0;'>75%</h4>
                <small>Profile Complete</small>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation Menu
    st.markdown("<h4 class='sidebar-title'>Navigation</h4>", unsafe_allow_html=True)
    
    # Create navigation links with icons and notifications
    nav_items = {
        "Home": {"icon": "🏠", "notifications": 0},
        "Career Assessment": {"icon": "📋", "notifications": 2},
        "Career Explorer": {"icon": "🔍", "notifications": 0},
        "Resources": {"icon": "📚", "notifications": 5},
        "Personal Dashboard": {"icon": "📊", "notifications": 1}
    }
    
    for nav_item, details in nav_items.items():
        is_active = st.session_state.page == nav_item
        notifications = details["notifications"]
        
        # Create the navigation link with conditional styling
        st.markdown(f"""
            <div class='nav-link {"active" if is_active else ""}'>
                <span>{details["icon"]}</span>
                <span style='flex-grow: 1;'>{nav_item}</span>
                {f'<span class="notification-badge">{notifications}</span>' if notifications > 0 else ''}
            </div>
        """, unsafe_allow_html=True)
        
        # Add the actual button (hidden but functional)
        if st.button(nav_item, key=f"nav_{nav_item}", help=f"Navigate to {nav_item}"):
            st.session_state.page = nav_item
    
    # Quick Stats
    st.markdown("---")
    st.markdown("<h4 class='sidebar-title'>Quick Stats</h4>", unsafe_allow_html=True)
    
    # Create two columns for stats
    stat_col1, stat_col2 = st.columns(2)
    
    with stat_col1:
        st.markdown("""
            <div style='text-align: center;'>
                <h4 style='color: #FF4B4B; margin: 0;'>5</h4>
                <small>Assessments</small>
            </div>
        """, unsafe_allow_html=True)
    
    with stat_col2:
        st.markdown("""
            <div style='text-align: center;'>
                <h4 style='color: #FF4B4B; margin: 0;'>12</h4>
                <small>Resources</small>
            </div>
        """, unsafe_allow_html=True)
    
    # Upcoming Tasks
    st.markdown("---")
    st.markdown("<h4 class='sidebar-title'>Upcoming Tasks</h4>", unsafe_allow_html=True)
    
    tasks = [
        {"title": "Complete Assessment", "due": "Today"},
        {"title": "Update Profile", "due": "Tomorrow"}
    ]
    
    for task in tasks:
        st.markdown(f"""
            <div style='padding: 0.5rem; background-color: white; border-radius: 5px; margin: 0.5rem 0;'>
                <small style='color: #666;'>{task['due']}</small>
                <p style='margin: 0;'>{task['title']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <div class='sidebar-footer'>
            <small style='color: #666;'>Need Help?</small>
            <br>
            <a href='#' style='color: #FF4B4B; text-decoration: none;'>Contact Support</a>
        </div>
    """, unsafe_allow_html=True)

# Main content
if st.session_state.page == "Home":
    # Hero Section
    st.markdown("""
        <div style='text-align: center; padding: 2rem 0;'>
            <h1 style='font-size: 3rem; margin-bottom: 1rem;'>Welcome to <span class='highlight'>MindForge</span> 🚀</h1>
            <p style='font-size: 1.2rem; color: #666; margin-bottom: 2rem;'>
                Your AI-Powered Career Guidance Companion
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Key Statistics
    st.markdown("### Platform Impact 📊")
    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
    
    with stats_col1:
        st.markdown("""
            <div class='stat-box'>
                <h2 style='color: #FF4B4B; font-size: 2rem;'>10K+</h2>
                <p>Students Guided</p>
            </div>
        """, unsafe_allow_html=True)
    
    with stats_col2:
        st.markdown("""
            <div class='stat-box'>
                <h2 style='color: #FF4B4B; font-size: 2rem;'>500+</h2>
                <p>Career Paths</p>
            </div>
        """, unsafe_allow_html=True)
    
    with stats_col3:
        st.markdown("""
            <div class='stat-box'>
                <h2 style='color: #FF4B4B; font-size: 2rem;'>95%</h2>
                <p>Success Rate</p>
            </div>
        """, unsafe_allow_html=True)
    
    with stats_col4:
        st.markdown("""
            <div class='stat-box'>
                <h2 style='color: #FF4B4B; font-size: 2rem;'>24/7</h2>
                <p>AI Support</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Interactive Demo Section
    st.markdown("---")
    demo_col1, demo_col2 = st.columns([2, 1])
    
    with demo_col1:
        st.markdown("### Try Our Quick Career Match! 🎯")
        interest_areas = st.multiselect(
            "Select your areas of interest:",
            ["Technology", "Science", "Arts", "Business", "Healthcare", "Education"],
            max_selections=3
        )
        
        skill_level = st.select_slider(
            "Rate your technical skills:",
            options=["Beginner", "Intermediate", "Advanced", "Expert"]
        )
        
        preferred_work = st.radio(
            "Preferred work environment:",
            ["Remote", "Office", "Hybrid", "Field Work"]
        )
        
        if st.button("Get Quick Career Match"):
            if interest_areas:
                st.success("Based on your preferences, here are some recommended career paths:")
                for area in interest_areas:
                    if area == "Technology":
                        st.write("🖥️ Software Development")
                        st.write("📊 Data Science")
                    elif area == "Science":
                        st.write("🔬 Research Scientist")
                        st.write("🧬 Biotechnology")
                    elif area == "Business":
                        st.write("📈 Business Analyst")
                        st.write("💼 Project Management")
    
    with demo_col2:
        st.image("https://img.freepik.com/free-vector/career-progress-concept-illustration_114360-5339.jpg",
                 caption="Discover Your Path")
        
        # Success Stories Counter
        st.markdown("""
            <div style='text-align: center; margin-top: 2rem;'>
                <h4>Success Stories Today</h4>
                <h2 style='color: #FF4B4B; font-size: 2.5rem;'>127</h2>
            </div>
        """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown("---")
    st.markdown("### How MindForge Helps You 🌟")
    
    features_col1, features_col2, features_col3 = st.columns(3)
    
    with features_col1:
        st.markdown("""
            <div class='feature-card'>
                <h3>🎯 Career Assessment</h3>
                <p>Take our comprehensive assessment to discover careers that match your interests, skills, and values.</p>
                <br/>
                <small style='color: #FF4B4B;'>20 minutes to complete</small>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Start Assessment", key="home_assessment"):
            st.session_state.page = "Career Assessment"
    
    with features_col2:
        st.markdown("""
            <div class='feature-card'>
                <h3>🔍 Career Explorer</h3>
                <p>Explore different career paths, required skills, and future prospects in various fields.</p>
                <br/>
                <small style='color: #FF4B4B;'>500+ career paths</small>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Explore Careers", key="home_explorer"):
            st.session_state.page = "Career Explorer"
    
    with features_col3:
        st.markdown("""
            <div class='feature-card'>
                <h3>📚 Learning Resources</h3>
                <p>Access curated resources, tutorials, and guidance materials for your chosen career path.</p>
                <br/>
                <small style='color: #FF4B4B;'>1000+ resources</small>
            </div>
        """, unsafe_allow_html=True)
        if st.button("View Resources", key="home_resources"):
            st.session_state.page = "Resources"
    
    # Testimonials Section
    st.markdown("---")
    st.markdown("### Success Stories 💫")
    
    testimonials_col1, testimonials_col2 = st.columns(2)
    
    with testimonials_col1:
        st.markdown("""
            <div style='padding: 1.5rem; border-left: 4px solid #FF4B4B; margin: 1rem 0;'>
                <p style='font-style: italic;'>"MindForge helped me discover my passion for data science. 
                Now I'm working at my dream company!"</p>
                <p style='color: #666;'>- Sarah P., Data Scientist</p>
            </div>
        """, unsafe_allow_html=True)
    
    with testimonials_col2:
        st.markdown("""
            <div style='padding: 1.5rem; border-left: 4px solid #FF4B4B; margin: 1rem 0;'>
                <p style='font-style: italic;'>"The career guidance I received was invaluable. 
                It helped me make an informed decision about my future."</p>
                <p style='color: #666;'>- James R., Software Engineer</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Call to Action
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; padding: 2rem 0;'>
            <h2>Ready to Start Your Journey? 🚀</h2>
            <p style='font-size: 1.2rem; color: #666; margin: 1rem 0;'>
                Join thousands of students who have found their perfect career path with MindForge
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    cta_col1, cta_col2, cta_col3 = st.columns([1, 2, 1])
    with cta_col2:
        if st.button("Begin Your Career Journey", key="home_cta"):
            st.session_state.page = "Career Assessment"

elif st.session_state.page == "Career Assessment":
    st.title("Career Assessment 📝")
    
    # Personal Information
    st.header("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=13, max_value=100)
    with col2:
        education = st.selectbox("Current Education Level", 
            ["High School", "Undergraduate", "Graduate", "Other"])
        location = st.text_input("Location")

    # Interest Assessment
    st.header("Interest Assessment")
    st.write("Rate your interest in the following areas (1-5):")
    
    interests = {
        "Technology": st.slider("Technology & Computing", 1, 5, 3),
        "Science": st.slider("Science & Research", 1, 5, 3),
        "Arts": st.slider("Arts & Creativity", 1, 5, 3),
        "Business": st.slider("Business & Management", 1, 5, 3),
        "Social": st.slider("Social Services & Teaching", 1, 5, 3)
    }
    
    if st.button("Generate Career Recommendations"):
        st.success("Based on your responses, here are some recommended career paths:")
        # Placeholder for recommendation logic
        st.write("1. Data Science & Analytics")
        st.write("2. Digital Marketing")
        st.write("3. Educational Technology")
        st.write("4. Healthcare Administration")
        st.write("5. Creative Design")

elif st.session_state.page == "Career Explorer":
    st.title("Career Explorer 🔍")
    
    # Career Categories
    categories = ["Technology", "Healthcare", "Business", "Education", "Creative Arts"]
    selected_category = st.selectbox("Select Career Category", categories)
    
    # Career Details (Placeholder data)
    careers = {
        "Technology": ["Software Developer", "Data Scientist", "Cybersecurity Analyst"],
        "Healthcare": ["Nurse Practitioner", "Medical Researcher", "Healthcare Administrator"],
        "Business": ["Financial Analyst", "Marketing Manager", "Entrepreneur"],
        "Education": ["Teacher", "Educational Consultant", "Instructional Designer"],
        "Creative Arts": ["Graphic Designer", "Content Creator", "UX Designer"]
    }
    
    selected_career = st.selectbox("Select Career", careers[selected_category])
    
    # Display career information
    st.header(f"About: {selected_career}")
    st.write("Career overview and detailed information would appear here...")
    
    # Skills Required
    st.subheader("Required Skills")
    st.write("Key skills for this career path...")
    
    # Job Market Trends
    st.subheader("Job Market Trends")
    # Placeholder chart
    data = pd.DataFrame({
        'Year': [2020, 2021, 2022, 2023, 2024],
        'Demand': [100, 120, 150, 180, 220]
    })
    fig = px.line(data, x='Year', y='Demand', title='Job Market Demand Trend')
    st.plotly_chart(fig)

elif st.session_state.page == "Resources":
    st.title("Learning Resources 📚")
    
    # Resource Categories
    st.header("Educational Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Online Courses")
        st.write("- Coursera")
        st.write("- edX")
        st.write("- Udemy")
        
        st.subheader("Certification Programs")
        st.write("- Professional Certifications")
        st.write("- Industry-specific Training")
        
    with col2:
        st.subheader("Career Development")
        st.write("- Resume Writing")
        st.write("- Interview Preparation")
        st.write("- Networking Tips")

elif st.session_state.page == "Personal Dashboard":
    st.title("Personal Dashboard 📊")
    
    # Profile Summary
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/businessman-character-avatar-isolated_24877-60111.jpg", 
                 width=200, caption="Profile Picture")
    with col2:
        st.subheader("Welcome back, User! 👋")
        st.write("Last login: Today at 10:00 AM")
        st.write("Career Path: Technology & Computing")
        st.write("Completed Assessments: 3/5")
    
    # Quick Actions
    st.markdown("---")
    quick_actions_col1, quick_actions_col2, quick_actions_col3 = st.columns(3)
    with quick_actions_col1:
        if st.button("📝 Take New Assessment"):
            st.session_state.page = "Career Assessment"
    with quick_actions_col2:
        if st.button("🎯 Update Goals"):
            st.session_state.show_goals = True
    with quick_actions_col3:
        if st.button("📚 Browse Resources"):
            st.session_state.page = "Resources"

    # Progress Overview
    st.markdown("---")
    st.subheader("Your Learning Journey 🚀")
    
    # Skill Development Progress with detailed breakdown
    progress_col1, progress_col2 = st.columns([2, 1])
    
    with progress_col1:
        st.markdown("### Skill Development")
        
        # Technical Skills
        tech_skills = {
            "Programming": 75,
            "Data Analysis": 60,
            "Web Development": 45,
            "Problem Solving": 80
        }
        
        for skill, value in tech_skills.items():
            col1, col2, col3 = st.columns([3, 6, 1])
            with col1:
                st.write(f"**{skill}**")
            with col2:
                st.progress(value/100)
            with col3:
                st.write(f"{value}%")
        
        # Soft Skills
        st.markdown("### Soft Skills")
        soft_skills = {
            "Communication": 85,
            "Leadership": 70,
            "Teamwork": 90,
            "Time Management": 65
        }
        
        for skill, value in soft_skills.items():
            col1, col2, col3 = st.columns([3, 6, 1])
            with col1:
                st.write(f"**{skill}**")
            with col2:
                st.progress(value/100)
            with col3:
                st.write(f"{value}%")
    
    with progress_col2:
        # Overall Progress Chart
        st.markdown("### Overall Progress")
        progress_data = pd.DataFrame({
            'Category': ['Technical', 'Soft Skills', 'Projects', 'Certifications'],
            'Progress': [65, 78, 45, 30]
        })
        
        fig = px.pie(progress_data, values='Progress', names='Category',
                    title='Progress Distribution',
                    hole=0.3,
                    color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig, use_container_width=True)

    # Goals and Milestones
    st.markdown("---")
    st.subheader("Goals & Milestones 🎯")
    
    # Timeline of goals
    timeline_col1, timeline_col2 = st.columns([3, 1])
    
    with timeline_col1:
        goals = {
            "Short-term Goals": [
                {"goal": "Complete Python Certification", "deadline": "2 weeks", "progress": 60},
                {"goal": "Finish Portfolio Project", "deadline": "1 month", "progress": 30}
            ],
            "Long-term Goals": [
                {"goal": "Master Data Science", "deadline": "6 months", "progress": 25},
                {"goal": "Land Dream Job", "deadline": "1 year", "progress": 15}
            ]
        }
        
        for goal_type, goal_list in goals.items():
            st.markdown(f"### {goal_type}")
            for goal in goal_list:
                col1, col2, col3, col4 = st.columns([3, 2, 4, 1])
                with col1:
                    st.write(f"**{goal['goal']}**")
                with col2:
                    st.write(f"Due: {goal['deadline']}")
                with col3:
                    st.progress(goal['progress']/100)
                with col4:
                    st.write(f"{goal['progress']}%")
    
    with timeline_col2:
        if st.button("➕ Add New Goal"):
            st.session_state.show_add_goal = True

    # Achievements Section
    st.markdown("---")
    st.subheader("Recent Achievements 🏆")
    
    achievements_col1, achievements_col2, achievements_col3 = st.columns(3)
    
    with achievements_col1:
        st.markdown("""
        🌟 **Skills Mastered**
        - Python Programming
        - Data Analysis
        - Project Management
        """)
    
    with achievements_col2:
        st.markdown("""
        📜 **Certifications**
        - Web Development Basics
        - Agile Methodology
        - Leadership 101
        """)
    
    with achievements_col3:
        st.markdown("""
        🎯 **Completed Goals**
        - Created Portfolio
        - Completed 5 Projects
        - Joined Tech Community
        """)

    # Activity Calendar
    st.markdown("---")
    st.subheader("Activity Calendar 📅")
    
    # Sample activity data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    activities = np.random.randint(0, 5, size=len(dates))
    activity_data = pd.DataFrame({
        'date': dates,
        'activity': activities
    })
    
    fig = px.scatter(activity_data, x='date', y='activity',
                    title='Your Learning Activity',
                    labels={'date': 'Date', 'activity': 'Activity Level'},
                    color='activity',
                    size='activity')
    st.plotly_chart(fig)

    # Recommendations
    st.markdown("---")
    st.subheader("Personalized Recommendations 💡")
    
    rec_col1, rec_col2 = st.columns(2)
    
    with rec_col1:
        st.markdown("""
        ### Suggested Next Steps
        1. Complete Python Advanced Course
        2. Start Machine Learning Project
        3. Join Tech Community Events
        """)
    
    with rec_col2:
        st.markdown("""
        ### Trending in Your Field
        1. AI/ML Development
        2. Cloud Computing
        3. Data Engineering
        """) 
