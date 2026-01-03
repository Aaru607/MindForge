from typing import Dict, List
from datetime import datetime, timedelta

class LearningPathGenerator:
    """Generate personalized learning roadmaps"""
    
    def __init__(self, ai_advisor):
        self.ai_advisor = ai_advisor
    
    async def create_learning_path(
        self,
        user_profile: Dict,
        target_career: Dict,
        current_skills: List[str],
        assessment_scores: Dict
    ) -> Dict:
        """Create a comprehensive learning path"""
        required_skills = set(target_career.get('required_skills', []))
        current_skills_set = set(current_skills)
        skill_gaps = list(required_skills - current_skills_set)
        
        # Get AI-generated learning plan
        ai_plan = await self.ai_advisor.generate_learning_plan(
            user_profile,
            target_career,
            skill_gaps
        )
        learning_path = {
            "user_id": user_profile['user_id'],
            "target_career": target_career['title'],
            "career_id": target_career['career_id'],
            "skill_gaps": skill_gaps,
            "estimated_duration": "6 months",
            "phases": [],
            "created_at": datetime.now().isoformat()
        }
        
        # Convert AI plan to structured phases
        for phase_key, phase_data in ai_plan.items():
            phase = {
                "name": phase_key.replace('_', ' ').title(),
                "duration": self._extract_duration(phase_key),
                "focus": phase_data.get('focus', ''),
                "skills_to_learn": phase_data.get('skills', []),
                "learning_resources": phase_data.get('resources', []),
                "milestones": self._generate_milestones(phase_data)
            }
            learning_path['phases'].append(phase)
        
        # Add career-specific certifications
        learning_path['recommended_certifications'] = self._get_certifications(target_career)
        
        # Add networking opportunities
        learning_path['networking'] = self._get_networking_tips(target_career)
        
        return learning_path
    
    def _extract_duration(self, phase_key: str) -> str:
        """Extract duration from phase key"""
        if 'months_1_2' in phase_key:
            return "Months 1-2"
        elif 'months_3_4' in phase_key:
            return "Months 3-4"
        elif 'months_5_6' in phase_key:
            return "Months 5-6"
        return "Unknown"
    
    def _generate_milestones(self, phase_data: Dict) -> List[Dict]:
        skills = phase_data.get('skills', [])
        milestones = []
        
        for skill in skills:
            milestones.append({
                "skill": skill,
                "goal": f"Achieve proficiency in {skill}",
                "validation": "Complete project demonstrating this skill"
            })
        
        return milestones
    
    def _get_certifications(self, career: Dict) -> List[Dict]:
        """Get relevant certifications for a career"""
        certification_map = {
            "Software Engineer": [
                {"name": "AWS Certified Developer", "provider": "Amazon", "priority": "high"},
                {"name": "Professional Scrum Developer", "provider": "Scrum.org", "priority": "medium"}
            ],
            "Data Scientist": [
                {"name": "TensorFlow Developer Certificate", "provider": "Google", "priority": "high"},
                {"name": "Azure Data Scientist Associate", "provider": "Microsoft", "priority": "high"}
            ],
            "Product Manager": [
                {"name": "Certified Scrum Product Owner", "provider": "Scrum Alliance", "priority": "high"},
                {"name": "Product Management Certificate", "provider": "General Assembly", "priority": "medium"}
            ]
        }
        
        return certification_map.get(career['title'], [
            {"name": "Industry-specific certification", "provider": "Research based on career", "priority": "medium"}
        ])
    
    def _get_networking_tips(self, career: Dict) -> List[str]:
        return [
            f"Join LinkedIn groups for {career['title']} professionals",
            f"Attend local {career['category']} meetups and conferences",
            "Connect with 3-5 professionals in this field for informational interviews",
            "Participate in online communities (Reddit, Discord, Slack groups)",
            "Contribute to open-source projects or industry forums"
        ]
