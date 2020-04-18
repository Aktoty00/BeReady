from rest_framework import mixins, generics

from ..models import StudentWorkPost, NewsPost, \
    NewsDiscussion, Lesson
from ..serializers import StudentWorkPostSerializer, NewsPostLongSerializer, \
    NewsDiscussionLongSerializer, LessonLongSerializer


class StudentWorkPostAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = StudentWorkPost.objects.all()
    serializer_class = StudentWorkPostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NewsPostAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,  generics.GenericAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostLongSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NewsDiscussionAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = NewsDiscussion.objects.all()
    serializer_class = NewsDiscussionLongSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LessonAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonLongSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

