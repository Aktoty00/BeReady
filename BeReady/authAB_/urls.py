from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from authAB_.views.cbv import TeacherAPIView, StudentAPIView
from authAB_.views.fbv import teacher_detail, student_detail
from authAB_.views.viewsets import TeacherViewSet, StudentViewSet, TeachersLesson, \
    StudentsLesson, StudentProfile, TeacherProfile


router = DefaultRouter()

router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'teachersLesson', TeachersLesson)
router.register(r'studentsLesson', StudentsLesson)
router.register(r'studentProfile', StudentProfile)
router.register(r'teacherProfile', TeacherProfile)

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('teacher/<int:pk>/detail/', teacher_detail),
    path('student/<int:pk>/detail/', student_detail),
    path('teacherRegister/', TeacherAPIView.as_view()),
    path('studentsRegister/', StudentAPIView.as_view()),
] + router.urls
