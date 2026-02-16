from django.urls import path
from . import views
from .views import Home, AddStudent, UpdateStudent, DeleteStudent

urlpatterns = [
    path("", Home.as_view(), name="home"),

    path("signup/", views.signupPage, name="signup"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutPage, name="logout"),

    path("add-student/", AddStudent.as_view(), name="add-student"),
    path("update-student/<int:id>/", UpdateStudent.as_view(), name="update-student"),
    path("delete-student/", DeleteStudent.as_view(), name="delete-student"),
]
