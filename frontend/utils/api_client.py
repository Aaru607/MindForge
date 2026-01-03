import requests
import os
from typing import Dict, List, Optional

class APIClient:
    """Client for backend API communication"""
    
    def __init__(self):
        self.base_url = os.getenv('BACKEND_URL', 'http://localhost:8000')
        self.token = None
    
    def set_token(self, token: str):
        """Set authentication token"""
        self.token = token
    
    def _get_headers(self) -> Dict:
        """Get request headers"""
        headers = {'Content-Type': 'application/json'}
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'
        return headers
    
    def submit_assessment(self, user_id: str, answers: List[Dict]) -> Dict:
        """Submit assessment answers"""
        try:
            response = requests.post(
                f"{self.base_url}/api/assessment/complete",
                json={"user_id": user_id, "answers": answers},
                headers=self._get_headers()
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API Error: {e}")
            return {"error": str(e)}
    
    def get_recommendations(self, user_id: str) -> List[Dict]:
        """Get career recommendations"""
        try:
            response = requests.post(
                f"{self.base_url}/api/recommendations/generate",
                json={"user_id": user_id, "max_results": 5},
                headers=self._get_headers()
            )
            response.raise_for_status()
            return response.json().get('recommendations', [])
        except requests.RequestException as e:
            print(f"API Error: {e}")
            return []
    
    def get_learning_path(self, user_id: str, career_id: int) -> Dict:
        """Get personalized learning path"""
        try:
            response = requests.get(
                f"{self.base_url}/api/learning-path/{user_id}/{career_id}",
                headers=self._get_headers()
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API Error: {e}")
            return {}
