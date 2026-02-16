from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from core.jwt_views import CustomTokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Web app routes
    path("", include("core.urls")),

    # API routes
    path("api/", include("core.api_urls")),

    # JWT Auth routes
    path("api/auth/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
