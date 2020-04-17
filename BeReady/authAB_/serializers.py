from rest_framework import serializers

from .models import MyUser, Teacher, Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'first_name', 'last_name')

    def validate(self, attrs):
        return attrs


class StudentSerializer(UserSerializer):
    stage = serializers.CharField(required=True)
    age = serializers.IntegerField()
    password = serializers.CharField(write_only=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('stage', 'password', 'age')

    def create(self, validated_data):
        student = Student.objects.create_user(username=validated_data['username'],
                                              first_name=validated_data.get('first_name', ''),
                                              last_name=validated_data.get('last_name', ''),
                                              address=validated_data.get('address', ''))
        student.set_password(validated_data['password'])
        student.save()
        return student


class TeacherSerializer(UserSerializer):
    level = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('level', 'password', 'email')

    def create(self, validated_data):
        teacher = Teacher.objects.create_user(username=validated_data['username'],
                                          first_name=validated_data.get('first_name', ''),
                                          last_name=validated_data.get('last_name', ''),
                                          address=validated_data.get('address', ''))
        teacher.set_password(validated_data['password'])
        teacher.save()
        return teacher

