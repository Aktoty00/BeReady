from rest_framework import serializers

from BeReady.BeReady.authAB_.serializers import TeacherSerializer, StudentSerializer
from BeReady.BeReady.core.models import Discussion, Post, Class


class DiscussionSerializer(serializers.Serializer):
    comment = serializers.CharField(required=True)
    date = serializers.DateField()
    # owner =

    def create(self, validated_data):
        discussion = Discussion(**validated_data)
        discussion.save()
        return discussion

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    date = serializers.DateField()
    # owner =
    discussion = DiscussionSerializer
    file = serializers.FileField()

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ClassShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('name', 'classCode', 'subject')

    def validate(self, attrs):
        return attrs


class ClassLongSerializer(ClassShortSerializer):
    owner = TeacherSerializer
    student = StudentSerializer
    post = PostSerializer

    class Meta(ClassShortSerializer.Meta):
        fields = ClassShortSerializer.Meta.fields + ('owner', 'student', 'post')
