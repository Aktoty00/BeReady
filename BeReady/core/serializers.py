from rest_framework import serializers

from authAB_.serializers import TeacherSerializer, StudentSerializer
from .models import StudentWorkPost, NewsPost, StudentWorkDiscussionWithReply, \
    StudentWorkDiscussionWithoutReply, NewsDiscussion, Lesson


class StudentWorkPostSerializer(serializers.ModelSerializer):
    owner = TeacherSerializer(read_only=True)

    class Meta:
        model = StudentWorkPost
        fields = ('title', 'description', 'date', 'owner', 'file')

    def validate(self, attrs):
        return attrs


class NewsPostShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = ('title', 'description', 'date')

    def validate(self, attrs):
        return attrs


class NewsPostLongSerializer(NewsPostShortSerializer):
    owner = TeacherSerializer(read_only=True)

    class Meta(NewsPostShortSerializer.Meta):
        fields = NewsPostShortSerializer.Meta.fields + ('owner', 'file')

    def validate(self, attrs):
        return attrs


class DiscussionWithReplySerializer(serializers.ModelSerializer):
    owner = StudentSerializer(read_only=True)
    sendTo = TeacherSerializer(read_only=True)

    class Meta:
        model = StudentWorkDiscussionWithReply
        fields = ('comment', 'date', 'sendTo', 'owner', 'post')

    def validate(self, attrs):
        return attrs


class DiscussionWithoutReplySerializer(serializers.ModelSerializer):
    owner = StudentSerializer(read_only=True)

    class Meta:
        model = StudentWorkDiscussionWithoutReply
        fields = ('comment', 'date', 'owner', 'post')

    def validate(self, attrs):
        return attrs


class NewsDiscussionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDiscussion
        fields = ('comment', 'date')

    def validate(self, attrs):
        return attrs


class NewsDiscussionLongSerializer(NewsDiscussionShortSerializer):
    owner = StudentSerializer(read_only=True)

    class Meta(NewsDiscussionShortSerializer.Meta):
        fields = NewsDiscussionShortSerializer.Meta.fields + ('owner', 'post')

    def validate(self, attrs):
        return attrs


class LessonShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('name', 'classCode', 'subject')

    def validate(self, attrs):
        return attrs


class LessonLongSerializer(LessonShortSerializer):
    owner = TeacherSerializer(read_only=True)
    students = StudentSerializer(read_only=True)

    class Meta(LessonShortSerializer.Meta):
        fields = LessonShortSerializer.Meta.fields + ('owner', 'students')
