from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer
from .utils import api_response


class RegisterAPI(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return api_response(
            data={"id": user.id, "username": user.username},
            message="Register success",
            status_code=status.HTTP_201_CREATED,
            success=True,
        )


class MeAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return api_response(
            data={"id": request.user.id, "username": request.user.username},
            message="User info",
            status_code=200,
            success=True,
        )
