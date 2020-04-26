import logging

from rest_framework import serializers

from authAB_.models import Teacher
from authAB_.serializers import TeacherSerializer, StudentSerializer, UserSerializer
from .models import StudentWorkPost, NewsPost, StudentWorkDiscussion, \
    NewsDiscussion, Lesson

logger = logging.getLogger(__name__)


class SWPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentWorkPost
        fields = ('id', 'title', 'description', 'date', 'owner')

    def validate(self, attrs):
        return attrs


class StudentWorkDiscussionSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    comment = serializers.CharField(required=True)
    date = serializers.DateTimeField(read_only=True)
    post = SWPostSerializer(read_only=True)
    post_id = serializers.IntegerField(write_only=True)
    owner = UserSerializer(default=serializers.CurrentUserDefault())
    sendTo = TeacherSerializer(read_only=True)
    sendTo_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        student_work_discussion = StudentWorkDiscussion(**validated_data)
        student_work_discussion.save()
        return student_work_discussion

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

    def validate_comment(self, value):
        if '$' in value:
            logger.error(f'Invalid char detected in comment: {value}')
            raise serializers.ValidationError('Invalid char detected in comment')
        if len(value) == 0:
            logger.error(f'Comment is empty')
            raise serializers.ValidationError('Comment is empty, write something')
        return value


class NewsDiscussionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDiscussion
        fields = ('id', 'comment', 'date')

    def validate(self, attrs):
        return attrs


class NewsDiscussionLongSerializer(NewsDiscussionShortSerializer):
    owner = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta(NewsDiscussionShortSerializer.Meta):
        fields = NewsDiscussionShortSerializer.Meta.fields + ('owner', 'post', 'owner_id')

    def validate(self, attrs):
        return attrs


class StudentWorkPostSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    date = serializers.DateTimeField(read_only=True)
    owner = UserSerializer(default=serializers.CurrentUserDefault())
    file = serializers.FileField(required=False)
    studentWorkDiscussion_post = StudentWorkDiscussionSerializer(many=True, required=False)

    def create(self, validated_data):
        student_work_post = StudentWorkPost(**validated_data)
        student_work_post.save()
        return student_work_post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def validate_title(self, value):
        if '/' in value:
            logger.error(f'Invalid char in title: {value}')
            raise serializers.ValidationError('Title can not have a slash')
        if len(value) == 0:
            logger.error(f'Title is empty')
            raise serializers.ValidationError('Title can not be empty, please write something')
        return value


class NewsPostShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = ('id', 'title', 'description', 'date')

    def validate(self, attrs):
        return attrs

    def validate_file(self, value):
        if value is None:
            logger.error(f'File has not selected')
            raise serializers.ValidationError('Please, upload a file')
        return value


class NewsPostLongSerializer(NewsPostShortSerializer):
    owner = UserSerializer(default=serializers.CurrentUserDefault())
    newsDiscussion_post = NewsDiscussionLongSerializer(many=True, required=False)

    class Meta(NewsPostShortSerializer.Meta):
        fields = NewsPostShortSerializer.Meta.fields + ('owner', 'file', 'newsDiscussion_post')

    def validate(self, attrs):
        return attrs


class LessonShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'classCode', 'subject')

    def validate(self, attrs):
        return attrs


class TeacherLessonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    mobile = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    age = serializers.IntegerField(read_only=True)
    level = serializers.CharField(read_only=True)
    lessons = LessonShortSerializer(many=True, required=False)

    def create(self, validated_data):
        new_teacher = Teacher(**validated_data)
        new_teacher.save()
        return new_teacher


class StudentLessonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    mobile = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    age = serializers.IntegerField(read_only=True)
    stage = serializers.CharField(read_only=True)
    lessons = LessonShortSerializer(many=True, required=False)

    def create(self, validated_data):
        new_student = Teacher(**validated_data)
        new_student.save()
        return new_student


class LessonLongSerializer(LessonShortSerializer):
    owner = TeacherSerializer(read_only=True)
    owner_id = serializers.IntegerField(write_only=True)
    students = StudentSerializer(read_only=True)
    students_id = serializers.IntegerField(write_only=True)
    posts = SWPostSerializer(many=True, required=False)

    class Meta(LessonShortSerializer.Meta):
        fields = LessonShortSerializer.Meta.fields + ('owner', 'students', 'owner_id', 'students_id')

    def validate_subject(self, value):
        if len(value) == 0:
            logger.error(f'Subject is empty')
            raise serializers.ValidationError('Subject name can not be empty, please write something')
        return value
