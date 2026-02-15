from django.urls import path
from .views import Home, AddStudent, DeleteStudent, UpdateStudent

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-student/', AddStudent.as_view(), name='add-student'),
    path('delete-student/', DeleteStudent.as_view(), name='delete-student'),
    path('update-student/<int:id>/', UpdateStudent.as_view(), name='update-student'),
]
