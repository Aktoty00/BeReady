from rest_framework import mixins, generics

from .models import StudentWorkPost, NewsPost, StudentWorkDiscussion, \
    NewsDiscussion, Lesson
from .serializers import StudentWorkPostSerializer, NewsPostLongSerializer, DiscussionWithReplySerializer, \
    NewsDiscussionLongSerializer, LessonLongSerializer


class StudentWorkPostAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = StudentWorkPost.objects.all()
    serializer_class = StudentWorkPostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NewsPostAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostLongSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DiscussionWithReplyAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = StudentWorkDiscussion.objects.all()
    serializer_class = DiscussionWithReplySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NewsDiscussionAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = NewsDiscussion.objects.all()
    serializer_class = NewsDiscussionLongSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class LessonAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonLongSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

