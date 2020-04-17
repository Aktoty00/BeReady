from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from authAB_.views.cbv import TeacherAPIView, StudentAPIView
from authAB_.views.fbv import teacher_detail, student_detail

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('teachers/', TeacherAPIView.as_view()),
    path('teachers/<int:pk>/', teacher_detail),
    path('students/<int:pk>/', student_detail),
    path('teacherRegister/', TeacherAPIView.as_view()),
    path('students/', StudentAPIView.as_view()),
    path('studentsRegister/', StudentAPIView.as_view())
]