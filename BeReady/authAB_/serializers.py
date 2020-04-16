from rest_framework import serializers

from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email')

    def validate(self, attrs):
        return attrs


class StudentSerializer(UserSerializer):
    stage = serializers.CharField(required=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('username', 'stage')


class TeacherSerializer(UserSerializer):
    level = serializers.CharField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('username', 'level')

