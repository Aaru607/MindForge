from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List, Dict
from datetime import datetime
from enum import Enum

class EducationLevel(str, Enum):
    HIGH_SCHOOL = "high_school"
    DIPLOMA = "diploma"
    UNDERGRADUATE = "undergraduate"
    GRADUATE = "graduate"
    POSTGRADUATE = "postgraduate"

class UserProfile(BaseModel):
    """User profile data model"""
    user_id: str
    email: EmailStr
    name: str
    age: Optional[int] = Field(None, ge=13, le=100)
    education_level: Optional[EducationLevel] = None
    current_field: Optional[str] = None
    location: Optional[str] = None
    interests: List[str] = []
    skills: List[str] = []
    career_goals: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    @validator('age')
    def validate_age(cls, v):
        if v and (v < 13 or v > 100):
            raise ValueError('Age must be between 13 and 100')
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user_123",
                "email": "student@example.com",
                "name": "John Doe",
                "age": 20,
                "education_level": "undergraduate",
                "interests": ["technology", "design", "business"]
            }
        }
