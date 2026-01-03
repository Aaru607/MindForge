🧠 MindForge – AI-Assisted Career Guidance Platform

--

MindForge is a data-driven career guidance platform designed to help students make informed career decisions through structured assessments and explainable recommendations.

--

🚀 Installation

--

-- Ensure Python 3.9+ is installed on your system

-- Clone the repository
git clone https://github.com/your-username/MindForge.git
cd MindForge

-- Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

-- Install project dependencies
pip install -r requirements.txt


--

▶️ Running the Application

--

-- Start the backend service
cd backend
uvicorn main:app --reload

-- Start the frontend application
cd frontend
streamlit run app.py

-- Access the application in your browser
http://localhost:8501


--

🧪 Testing

--

-- Run backend unit tests
pytest backend/tests/ -v


--

📁 Project Structure

--

-- High-level repository layout
mindforge/
├── backend/                 # FastAPI backend services
├── frontend/                # Streamlit application
├── scripts/                 # Utility scripts
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation


--

✅ Why This Format Works

-- acts like inline command annotations

Commands remain copy-paste friendly

Looks like real engineering runbooks

Clear separation between instruction and command

Reviewers immediately understand execution flow

This is not markdown misuse — it’s a deliberate documentation style.

❗ One Important Rule (Follow This)

✔ Keep -- inside code blocks only
❌ Do NOT mix -- with markdown bullets outside code blocks

You’ve done it correctly here.
