import logging

from rest_framework import mixins, viewsets, serializers

from authAB_.models import Teacher
from ..models import StudentWorkPost, NewsPost, StudentWorkDiscussion, NewsDiscussion
from ..serializers import StudentWorkPostSerializer, NewsPostLongSerializer, \
    StudentWorkDiscussionSerializer, NewsDiscussionLongSerializer

logger = logging.getLogger(__name__)


class StudentWorkPostDetail(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    queryset = StudentWorkPost.objects.all()
    serializer_class = StudentWorkPostSerializer

    def create(self, request, *args, **kwargs):
        teachers = Teacher.objects.all()
        is_teacher = False
        for teacher in teachers:
            if request.user.id == teacher.id:
                is_teacher = True
        if is_teacher:
            return self.create(request, *args, **kwargs)
        else:
            raise serializers.ValidationError('Invalid account, you have not access to do something,'
                                              ' because you are not teacher')

    def update(self, request, *args, **kwargs):
        teachers = Teacher.objects.all()
        is_teacher = False
        for teacher in teachers:
            if request.user.id == teacher.id:
                is_teacher = True
        if is_teacher:
            return self.update(request, *args, **kwargs)
        else:
            raise serializers.ValidationError('Invalid account, you have not access to do something,'
                                              ' because you are not teacher')

    def destroy(self, request, *args, **kwargs):
        teachers = Teacher.objects.all()
        is_teacher = False
        for teacher in teachers:
            if request.user.id == teacher.id:
                is_teacher = True
        if is_teacher:
            return self.destroy(request, *args, **kwargs)
        else:
            raise serializers.ValidationError('Invalid account, you have not access to do something,'
                                              ' because you are not teacher')

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'StudentWorkPost object created, title: {serializer.instance.title}')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'StudentWorkPost object updated, title: {serializer.instance.title}')


class NewsPostDetail(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostLongSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'NewsPost object created, title: {serializer.instance.title}')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'NewsPost object updated, title: {serializer.instance.title}')


class SWDiscussionsViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = StudentWorkDiscussion.objects.all()
    serializer_class = StudentWorkDiscussionSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'StudentWorkDiscussions object created, comment: {serializer.instance.comment}')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'StudentWorkDiscussions object updated, comment: {serializer.instance.comment}')


class NewsDiscussionsViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.CreateModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    queryset = NewsDiscussion.objects.all()
    serializer_class = NewsDiscussionLongSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'NewsDiscussions object created, comment: {serializer.instance.comment}')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'NewsDiscussions object updated, comment: {serializer.instance.comment}')
