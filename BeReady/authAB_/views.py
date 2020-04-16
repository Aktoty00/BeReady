from rest_framework import mixins, generics

from .models import Teacher, Student
from .serializers import TeacherSerializer, StudentSerializer


class TeacherAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StudentAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

