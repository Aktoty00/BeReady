import logging

from rest_framework import mixins
from rest_framework import viewsets

from core.serializers import TeacherLessonSerializer, StudentLessonSerializer
from ..models import Student, Teacher, StudentProfile, TeacherProfile
from ..serializers import StudentSerializer, TeacherSerializer, StudentProfileSerializer, TeacherProfileSerializer

logger = logging.getLogger(__name__)


class TeacherViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'Teacher object created, username: {serializer.instance.username}')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Teacher object updated, username: {serializer.instance.username}')


class StudentViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'Student object created, username: {serializer.instance.username}')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Student object updated, username: {serializer.instance.username}')


class TeachersLesson(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherLessonSerializer


class StudentsLesson(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentLessonSerializer


class StudentProfile(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class TeacherProfile(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
