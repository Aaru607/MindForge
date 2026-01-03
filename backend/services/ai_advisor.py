import os
from typing import Dict, List
import anthropic
from datetime import datetime

class AICareerAdvisor:
    """AI-powered career guidance using Claude API"""
    
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.model = "claude-sonnet-4-20250514"
    
    async def generate_career_advice(
        self,
        user_profile: Dict,
        assessment_scores: Dict,
        career: Dict
    ) -> str:
        """Generate personalized career advice using AI"""
        
        prompt = f"""You are an experienced career counselor helping a student explore their career options.

User Profile:
- Name: {user_profile.get('name')}
- Education: {user_profile.get('education_level')}
- Interests: {', '.join(user_profile.get('interests', []))}
- Goals: {user_profile.get('career_goals', 'Not specified')}

Assessment Results:
- Primary Aptitude: {assessment_scores.get('primary_aptitude')}
- Primary Interest: {assessment_scores.get('primary_interest')}
- Top Skills: {', '.join(list(assessment_scores.get('skill_levels', {}).keys())[:3])}

Career Being Considered: {career['title']}

Provide personalized, actionable career advice that:
1. Explains why this career aligns with their strengths
2. Identifies 2-3 specific skill gaps they should address
3. Suggests 3 concrete next steps they can take this month
4. Offers encouragement and realistic expectations

Keep the tone warm, supportive, and motivating. Be specific and actionable."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return response.content[0].text
            
        except Exception as e:
            print(f"AI advice generation failed: {e}")
            return self._fallback_advice(career)
    
    def _fallback_advice(self, career: Dict) -> str:
        """Fallback advice if AI call fails"""
        return f"""Based on your assessment results, {career['title']} appears to be a strong match for your profile.

Key Strengths:
- Your aptitude scores align well with the core requirements
- Your interests match the typical work activities in this field

Recommended Next Steps:
1. Research 3-5 professionals currently working in this role
2. Identify the most in-demand skills for this career
3. Consider entry-level positions or internships to gain experience

This career offers {career['growth_outlook']} growth potential and has {career['demand']} market demand."""
    
    async def generate_learning_plan(
        self,
        user_profile: Dict,
        target_career: Dict,
        skill_gaps: List[str]
    ) -> Dict:
        """Generate a personalized learning plan"""
        
        prompt = f"""Create a structured 6-month learning plan for someone wanting to enter: {target_career['title']}

Their current situation:
- Education: {user_profile.get('education_level')}
- Current skills: {', '.join(user_profile.get('skills', []))}

Skills they need to develop:
{', '.join(skill_gaps)}

Provide a JSON response with this structure:
{{
    "phase_1_months_1_2": {{
        "focus": "Foundation building",
        "skills": ["skill1", "skill2"],
        "resources": [
            {{"type": "course", "name": "Course name", "platform": "Platform", "duration": "4 weeks"}},
            {{"type": "project", "name": "Project name", "difficulty": "beginner"}}
        ]
    }},
    "phase_2_months_3_4": {{...}},
    "phase_3_months_5_6": {{...}}
}}"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1500,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            import json
            plan_text = response.content[0].text
            start = plan_text.find('{')
            end = plan_text.rfind('}') + 1
            plan_json = json.loads(plan_text[start:end])
            
            return plan_json
            
        except Exception as e:
            print(f"Learning plan generation failed: {e}")
            return self._fallback_learning_plan(skill_gaps)
    
    def _fallback_learning_plan(self, skill_gaps: List[str]) -> Dict:
        """Fallback learning plan if AI call fails"""
        return {
            "phase_1_months_1_2": {
                "focus": "Foundation Skills",
                "skills": skill_gaps[:2] if len(skill_gaps) >= 2 else skill_gaps,
                "resources": [
                    {"type": "online_course", "platform": "Coursera/Udemy", "duration": "4-6 weeks"},
                    {"type": "practice_project", "difficulty": "beginner"}
                ]
            },
            "phase_2_months_3_4": {
                "focus": "Intermediate Skills",
                "skills": skill_gaps[2:4] if len(skill_gaps) > 2 else ["Advanced concepts"],
                "resources": [
                    {"type": "certification", "platform": "Industry certification", "duration": "6-8 weeks"}
                ]
            },
            "phase_3_months_5_6": {
                "focus": "Real-World Application",
                "skills": ["Portfolio building", "Networking"],
                "resources": [
                    {"type": "capstone_project", "difficulty": "intermediate"},
                    {"type": "mentorship", "platform": "LinkedIn/Industry groups"}
                ]
            }
        }
