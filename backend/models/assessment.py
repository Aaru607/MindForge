from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum

class QuestionType(str, Enum):
    APTITUDE = "aptitude"
    INTEREST = "interest"
    PERSONALITY = "personality"
    SKILL = "skill"

class AssessmentQuestion(BaseModel):
    question_id: str
    type: QuestionType
    dimension: str 
    text: str
    options: List[Dict[str, str]] 
    weight: float = 1.0
    
class UserAnswer(BaseModel):
    question_id: str
    answer: str
    timestamp: datetime = Field(default_factory=datetime.now)

class AssessmentSession(BaseModel):
    session_id: str
    user_id: str
    status: str = "in_progress" 
    answers: List[UserAnswer] = []
    started_at: datetime = Field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None
    
class AssessmentScores(BaseModel):
    user_id: str
    aptitude_scores: Dict[str, float]  
    interest_profiles: Dict[str, float]
    personality_traits: Dict[str, float]
    skill_levels: Dict[str, float]
    primary_aptitude: str
    primary_interest: str
    calculated_at: datetime = Field(default_factory=datetime.now)
