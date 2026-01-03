import json
from typing import List, Dict
from motor.motor_asyncio import AsyncIOMotorClient
import os

class DatabaseSeeder:    
    def __init__(self, mongo_uri: str):
        self.client = AsyncIOMotorClient(mongo_uri)
        self.db = self.client['mindforge']
    
    async def seed_all(self):
        print("Starting database seeding...")
        await self.seed_careers()
        await self.seed_questions()
        await self.seed_skills_taxonomy()
        
        print("Database seeding completed!")
    
    async def seed_careers(self):
        """Seed careers collection"""
        careers = [
            {
                "career_id": 1,
                "title": "Software Engineer",
                "category": "Technology",
                "description": "Design, develop, and maintain software applications and systems",
                "required_aptitudes": ["analytical", "technical", "problem-solving"],
                "required_interests": ["investigative", "realistic"],
                "required_skills": ["Programming", "Data Structures", "Algorithms", "System Design"],
                "education_requirements": ["Bachelor's in Computer Science or related field"],
                "salary_range": "$80,000 - $150,000",
                "growth_outlook": "high",
                "demand": "high",
                "work_environment": "Office/Remote",
                "typical_tasks": [
                    "Write and review code",
                    "Design software architecture",
                    "Debug and optimize applications",
                    "Collaborate with team members"
                ]
            },
            {
                "career_id": 2,
                "title": "Data Scientist",
                "category": "Technology",
                "description": "Analyze complex data to help organizations make better decisions",
                "required_aptitudes": ["analytical", "mathematical", "technical"],
                "required_interests": ["investigative", "conventional"],
                "required_skills": ["Python", "Statistics", "Machine Learning", "Data Visualization"],
                "education_requirements": ["Bachelor's/Master's in Data Science, Statistics, or CS"],
                "salary_range": "$90,000 - $160,000",
                "growth_outlook": "high",
                "demand": "high",
                "work_environment": "Office/Remote",
                "typical_tasks": [
                    "Build predictive models",
                    "Analyze large datasets",
                    "Create data visualizations",
                    "Present insights to stakeholders"
                ]
            },
            {
                "career_id": 3,
                "title": "UX/UI Designer",
                "category": "Design",
                "description": "Create intuitive and aesthetically pleasing user interfaces",
                "required_aptitudes": ["creative", "analytical", "empathetic"],
                "required_interests": ["artistic", "social"],
                "required_skills": ["Design Tools (Figma, Adobe XD)", "User Research", "Prototyping"],
                "education_requirements": ["Bachelor's in Design, HCI, or related field"],
                "salary_range": "$60,000 - $120,000",
                "growth_outlook": "high",
                "demand": "medium",
                "work_environment": "Office/Remote",
                "typical_tasks": [
                    "Conduct user research",
                    "Create wireframes and prototypes",
                    "Design user interfaces",
                    "Conduct usability testing"
                ]
            },
            {
                "career_id": 4,
                "title": "Product Manager",
                "category": "Business",
                "description": "Define product strategy and guide development teams",
                "required_aptitudes": ["strategic", "communicative", "analytical"],
                "required_interests": ["enterprising", "social"],
                "required_skills": ["Product Strategy", "Agile", "User Stories", "Stakeholder Management"],
                "education_requirements": ["Bachelor's in Business, CS, or related field"],
                "salary_range": "$100,000 - $180,000",
                "growth_outlook": "high",
                "demand": "high",
                "work_environment": "Office/Hybrid",
                "typical_tasks": [
                    "Define product roadmap",
                    "Prioritize features",
                    "Coordinate with engineering",
                    "Analyze market trends"
                ]
            },
            {
                "career_id": 5,
                "title": "Digital Marketing Specialist",
                "category": "Marketing",
                "description": "Develop and execute online marketing campaigns",
                "required_aptitudes": ["creative", "analytical", "communicative"],
                "required_interests": ["enterprising", "artistic"],
                "required_skills": ["SEO", "Social Media Marketing", "Content Creation", "Analytics"],
                "education_requirements": ["Bachelor's in Marketing, Communications, or related field"],
                "salary_range": "$50,000 - $90,000",
                "growth_outlook": "medium",
                "demand": "medium",
                "work_environment": "Office/Remote",
                "typical_tasks": [
                    "Create marketing campaigns",
                    "Manage social media",
                    "Analyze campaign performance",
                    "Optimize SEO strategies"
                ]
            }
        ]
        
        collection = self.db['careers']
        await collection.delete_many({})  # Clear existing
        await collection.insert_many(careers)
        print(f"Seeded {len(careers)} careers")
    
    async def seed_questions(self):
        """Seed assessment questions"""
        questions = [
            # Aptitude Questions
            {
                "question_id": "apt_001",
                "type": "aptitude",
                "dimension": "analytical",
                "text": "You're given a complex problem with multiple variables. How do you approach it?",
                "options": [
                    {"key": "A", "text": "Break it into smaller parts and analyze each systematically"},
                    {"key": "B", "text": "Look for creative solutions and think outside the box"},
                    {"key": "C", "text": "Seek advice from others who've faced similar problems"},
                    {"key": "D", "text": "Try different approaches until something works"}
                ],
                "weight": 1.2
            },
            {
                "question_id": "apt_002",
                "type": "aptitude",
                "dimension": "creative",
                "text": "When working on a project, you prefer to:",
                "options": [
                    {"key": "A", "text": "Follow established procedures and best practices"},
                    {"key": "B", "text": "Experiment with new ideas and innovative approaches"},
                    {"key": "C", "text": "Collaborate and brainstorm with team members"},
                    {"key": "D", "text": "Focus on practical, efficient solutions"}
                ],
                "weight": 1.0
            },
            {
                "question_id": "apt_003",
                "type": "aptitude",
                "dimension": "technical",
                "text": "How comfortable are you learning new technical tools or software?",
                "options": [
                    {"key": "A", "text": "Very comfortable - I enjoy exploring new technologies"},
                    {"key": "B", "text": "Somewhat comfortable - I can learn when needed"},
                    {"key": "C", "text": "Uncomfortable - I prefer sticking to familiar tools"},
                    {"key": "D", "text": "Very uncomfortable - Technical tools frustrate me"}
                ],
                "weight": 1.3
            },
            # Interest Questions
            {
                "question_id": "int_001",
                "type": "interest",
                "dimension": "investigative",
                "text": "Rate your interest: Conducting research and analyzing data",
                "options": [
                    {"key": "1", "text": "Not interested"},
                    {"key": "2", "text": "Slightly interested"},
                    {"key": "3", "text": "Moderately interested"},
                    {"key": "4", "text": "Very interested"},
                    {"key": "5", "text": "Extremely interested"}
                ],
                "weight": 1.0
            },
            {
                "question_id": "int_002",
                "type": "interest",
                "dimension": "artistic",
                "text": "Rate your interest: Creating visual designs or artwork",
                "options": [
                    {"key": "1", "text": "Not interested"},
                    {"key": "2", "text": "Slightly interested"},
                    {"key": "3", "text": "Moderately interested"},
                    {"key": "4", "text": "Very interested"},
                    {"key": "5", "text": "Extremely interested"}
                ],
                "weight": 1.0
            },
            {
                "question_id": "int_003",
                "type": "interest",
                "dimension": "social",
                "text": "Rate your interest: Helping and teaching others",
                "options": [
                    {"key": "1", "text": "Not interested"},
                    {"key": "2", "text": "Slightly interested"},
                    {"key": "3", "text": "Moderately interested"},
                    {"key": "4", "text": "Very interested"},
                    {"key": "5", "text": "Extremely interested"}
                ],
                "weight": 1.0
            },
            {
                "question_id": "int_004",
                "type": "interest",
                "dimension": "enterprising",
                "text": "Rate your interest: Leading projects and persuading others",
                "options": [
                    {"key": "1", "text": "Not interested"},
                    {"key": "2", "text": "Slightly interested"},
                    {"key": "3", "text": "Moderately interested"},
                    {"key": "4", "text": "Very interested"},
                    {"key": "5", "text": "Extremely interested"}
                ],
                "weight": 1.0
            }
        ]
        
        collection = self.db['assessment_questions']
        await collection.delete_many({})
        await collection.insert_many(questions)
        print(f"Seeded {len(questions)} assessment questions")
    
    async def seed_skills_taxonomy(self):
        skills = {
            "technical_skills": {
                "programming": ["Python", "JavaScript", "Java", "C++", "Go"],
                "data": ["SQL", "NoSQL", "Data Analysis", "Machine Learning", "Big Data"],
                "design": ["Figma", "Adobe XD", "Sketch", "Photoshop", "Illustrator"],
                "devops": ["Docker", "Kubernetes", "CI/CD", "AWS", "Azure"]
            },
            "soft_skills": {
                "communication": ["Public Speaking", "Writing", "Presentations", "Active Listening"],
                "leadership": ["Team Management", "Decision Making", "Conflict Resolution"],
                "problem_solving": ["Critical Thinking", "Analytical Skills", "Creativity"],
                "collaboration": ["Teamwork", "Empathy", "Negotiation"]
            }
        }
        
        collection = self.db['skills_taxonomy']
        await collection.delete_many({})
        
