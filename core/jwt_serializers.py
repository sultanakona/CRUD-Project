from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .utils import api_response

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # custom wrapper like your other project
        return {
            "statusCode": 200,
            "success": True,
            "message": "Login success",
            "data": {
                "accessToken": data["access"],
                "refreshToken": data["refresh"],
            },
        }
