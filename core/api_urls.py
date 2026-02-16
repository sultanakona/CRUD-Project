from django.urls import path
from .api_views import RegisterAPI, MeAPI

urlpatterns = [
    path("auth/register/", RegisterAPI.as_view(), name="api_register"),
    path("auth/me/", MeAPI.as_view(), name="api_me"),
]
