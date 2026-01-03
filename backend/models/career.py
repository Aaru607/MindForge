from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Career(BaseModel):
    career_id: int
    title: str
    category: str
    description: str
    required_aptitudes: List[str]
    required_interests: List[str]
    required_skills: List[str]
    education_requirements: List[str]
    salary_range: str
    growth_outlook: str  
    demand: str  
    work_environment: str
    typical_tasks: List[str]
    
class CareerRecommendation(BaseModel):
    career_id: int
    career_title: str
    match_percentage: float
    reasoning: str
    strengths_alignment: List[str]
    gaps: List[str]
    salary_range: str
    growth_outlook: str
    recommended_resources: List[Dict[str, str]]
    next_steps: List[str]
    created_at: datetime = Field(default_factory=datetime.now)
class LearningPath(BaseModel):
    user_id: str
    career_id: int
    career_title: str
    current_skills: List[str]
    required_skills: List[str]
    skill_gaps: List[str]
    learning_modules: List[Dict]
    estimated_duration: str
    milestones: List[Dict]
    created_at: datetime = Field(default_factory=datetime.now)
