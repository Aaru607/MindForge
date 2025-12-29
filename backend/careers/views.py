from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import CareerAssessment
from .utils import process_career_csv
from .services import generate_recommendations
from users.models import UserProfile

class CareerAssessmentView(APIView):
    def post(self, request):
        user = UserProfile.objects.get(email=request.data["email"])
        recommendations = generate_recommendations(
            request.data["interests"],
            request.data["skill_level"]
        )
        CareerAssessment.objects.create(
            user=user,
            interests=request.data["interests"],
            skill_level=request.data["skill_level"],
            recommended_paths=recommendations
        )
        return Response({"recommendations": recommendations})
class AdminCareerUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        count = process_career_csv(request.FILES["file"])
        return Response({"records_processed": count})
