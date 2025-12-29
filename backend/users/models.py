from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
class UserCreateView(APIView):
    def post(self, request):
        user = UserProfile.objects.create(
            email=request.data["email"],
            full_name=request.data["full_name"]
        )
        return Response({"id": user.id})
