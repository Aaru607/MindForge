from django.urls import path
from .views import CareerAssessmentView, AdminCareerUploadView

urlpatterns = [
    path("assess/", CareerAssessmentView.as_view()),
    path("admin/upload/", AdminCareerUploadView.as_view()),
]
