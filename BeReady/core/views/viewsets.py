from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from authAB_.models import Student
from ..models import StudentWorkPost, NewsPost, StudentWorkDiscussion, \
    NewsDiscussion, Lesson
from ..serializers import StudentWorkPostSerializer, NewsPostLongSerializer, StudentWorkDiscussionSerializer, \
    NewsDiscussionLongSerializer, LessonLongSerializer


class student_work_post_detail(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.CreateModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    queryset = StudentWorkPost.objects.all()
    serializer_class = StudentWorkPostSerializer


class news_post_detail(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostLongSerializer
