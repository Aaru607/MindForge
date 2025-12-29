from django.db import models
from users.models import UserProfile
class CareerAssessment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    interests = models.JSONField()
    skill_level = models.CharField(max_length=50)
    recommended_paths = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
class CareerMaster(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    description = models.TextField()
    required_skills = models.JSONField()
    growth_score = models.IntegerField()
