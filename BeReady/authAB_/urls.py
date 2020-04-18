from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from authAB_.views.cbv import TeacherAPIView, StudentAPIView
from authAB_.views.viewsets import TeacherViewSet, StudentViewSet
router = DefaultRouter()

router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
urlpatterns = [
    path('login/', obtain_jwt_token),
    path('teacherRegister/', TeacherAPIView.as_view()),
    path('studentsRegister/', StudentAPIView.as_view()),
] + router.urls
