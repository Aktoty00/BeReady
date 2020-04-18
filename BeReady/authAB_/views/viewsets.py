import logging

from rest_framework import mixins
from rest_framework import viewsets

from ..models import Student, Teacher
from ..serializers import StudentSerializer, TeacherSerializer

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
