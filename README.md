🧠 MindForge – AI-Assisted Career Guidance Platform

MindForge is a data-driven career guidance platform designed to help students make informed career decisions through structured assessments and explainable recommendations. The platform focuses on transforming user assessment data into clear, actionable career insights using deterministic logic enhanced with AI-generated explanations.

✨ Features

📊 Structured Career Assessment
Multi-dimensional assessment covering aptitude and interest areas.

🎯 Personalized Career Recommendations
Deterministic, explainable ranking of careers based on assessment scores.

📚 Guided Learning Paths
Career-specific learning roadmaps highlighting skills to develop and next steps.

💡 AI-Assisted Guidance
AI is used to generate human-readable explanations and guidance, not for decision-making.

📈 User Profile & Progress Tracking
View assessment history, saved careers, and learning milestones.

🛠️ Tech Stack

Frontend: Streamlit

Backend: FastAPI (async APIs)

Database: MongoDB

AI Integration: Anthropic Claude (for explanations only)

Language: Python

🚀 Installation

Ensure Python 3.9+ is installed on your system.

Clone the repository:

git clone https://github.com/your-username/MindForge.git
cd MindForge


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

▶️ Running the Application
Start the Backend
cd backend
uvicorn main:app --reload

Start the Frontend
cd frontend
streamlit run app.py


The application will be available at:
http://localhost:8501

📁 Project Structure
mindforge/
├── backend/                 # FastAPI backend services
│   ├── api/                 # API routes
│   ├── services/            # Core business logic
│   ├── models/              # Data models
│   └── database/            # Database clients & seed scripts
│
├── frontend/                # Streamlit application
│   ├── pages/               # Multi-page UI
│   ├── components/          # Reusable UI components
│   └── utils/               # Session & API helpers
│
├── scripts/                 # Utility scripts
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

🧠 How MindForge Works

Users complete a structured career assessment.

Assessment scores are processed using deterministic scoring logic.

Careers are ranked based on aptitude and interest alignment.

AI generates explanations and guidance for the ranked results.

Users receive recommendations and personalized learning paths.

🧪 Testing

To run backend tests:

pytest backend/tests/ -v

🤝 Contributing

Contributions are welcome. Please open an issue or submit a pull request for improvements or fixes.

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
