from rest_framework import serializers
import authAB_.serializers
from authAB_.serializers import TeacherSerializer, StudentSerializer
from .models import StudentWorkPost, NewsPost, StudentWorkDiscussion, \
    NewsDiscussion, Lesson


class StudentWorkPostSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    date = serializers.DateTimeField(read_only=True)
    owner = authAB_.serializers.UserSerializer(default=serializers.CurrentUserDefault())
    file = serializers.FileField(required=False)

    def create(self, validated_data):
        student_work_post = StudentWorkPost(**validated_data)
        student_work_post.save()
        return student_work_post

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def validate_title(self, value):
        if '/' in value:
            raise serializers.ValidationError('Title can not have a slash')
        if len(value) == 0:
            raise serializers.ValidationError('Title can not be empty, please write something')
        return value


class NewsPostShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = ('title', 'description', 'date')

    def validate(self, attrs):
        return attrs

    def validate_file(self, value):
        if value is None:
            raise serializers.ValidationError('Please, upload a file')
        return value


class NewsPostLongSerializer(NewsPostShortSerializer):
    owner = authAB_.serializers.UserSerializer(default=serializers.CurrentUserDefault())

    class Meta(NewsPostShortSerializer.Meta):
        fields = NewsPostShortSerializer.Meta.fields + ('owner', 'file')

    def validate(self, attrs):
        return attrs


class StudentWorkDiscussionSerializer(serializers.Serializer):
    comment = serializers.CharField(required=True)
    date = serializers.DateTimeField(read_only=True)
    post = StudentWorkPostSerializer(read_only=True)
    post_id = serializers.IntegerField(write_only=True)
    owner = authAB_.serializers.UserSerializer(default=serializers.CurrentUserDefault())
    sendTo = TeacherSerializer(read_only=True)
    sendTo_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        student_work_discussion = StudentWorkDiscussion(**validated_data)
        student_work_discussion.save()
        return student_work_discussion

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def validate_comment(self, value):
        if ['$', '#', '~', '/', '%'] in value:
            raise serializers.ValidationError('invalid char detected in comment')
        if len(value):
            raise serializers.ValidationError('Comment is empty, write something')
        return value


class NewsDiscussionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDiscussion
        fields = ('comment', 'date')

    def validate(self, attrs):
        return attrs


class NewsDiscussionLongSerializer(NewsDiscussionShortSerializer):
    owner = authAB_.serializers.UserSerializer(default=serializers.CurrentUserDefault())

    class Meta(NewsDiscussionShortSerializer.Meta):
        fields = NewsDiscussionShortSerializer.Meta.fields + ('owner', 'post', 'owner_id')

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
    owner_id = serializers.IntegerField(write_only=True)
    students = StudentSerializer(read_only=True)
    students_id = serializers.IntegerField(write_only=True)

    class Meta(LessonShortSerializer.Meta):
        fields = LessonShortSerializer.Meta.fields + ('owner', 'students', 'owner_id', 'students_id')

    def validate_subject(self, value):
        if len(value) == 0:
            raise serializers.ValidationError('Subject name can not be empty, please write something')
        return value
