from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from authAB_.views import TeacherAPIView, StudentAPIView

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('teachers/', TeacherAPIView.as_view()),
    path('teacherRegister/', TeacherAPIView.as_view()),
    path('students/', StudentAPIView.as_view()),
    path('studentsRegister/', StudentAPIView.as_view())
]