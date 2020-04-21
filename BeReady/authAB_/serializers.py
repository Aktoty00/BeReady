import logging

from rest_framework import serializers

from .models import MyUser, Teacher, Student, STAGE, LEVEL

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'first_name', 'last_name')

    def validate(self, attrs):
        return attrs


class StudentSerializer(UserSerializer):
    STAGE = STAGE
    stage = serializers.CharField(required=True)
    age = serializers.IntegerField()
    password = serializers.CharField(write_only=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('stage', 'password', 'age')

    def create(self, validated_data):
        student = Student.objects.create_user(username=validated_data['username'],
                                              first_name=validated_data.get('first_name', ''),
                                              last_name=validated_data.get('last_name', ''),
                                              stage=validated_data.get('stage', ''),
                                              age=validated_data.get('age', ''))
        student.set_password(validated_data['password'])
        student.save()
        return student

    def validate_stage(self, value):
        if (value, value) not in STAGE:
            logger.error(f'Invalid choice for stage: {value}')
            raise serializers.ValidationError('Subject name can be only: Freshman, Sophomore, Junior, Senior')

        return value


class TeacherSerializer(UserSerializer):
    level = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('level', 'password', 'email')

    def create(self, validated_data):
        teacher = Teacher.objects.create_user(username=validated_data['username'],
                                          first_name=validated_data.get('first_name', ''),
                                          last_name=validated_data.get('last_name', ''),
                                          level=validated_data.get('level', ''),
                                          address=validated_data.get('address', ''))
        teacher.set_password(validated_data['password'])
        teacher.save()
        return teacher

    def validate_level(self, value):
        if (value, value) not in LEVEL:
            logger.error(f'Invalid choice for level: {value}')
            raise serializers.ValidationError('Level name can be only: Associate degree, Bachelor degree, '
                                              'Master degree, Doctoral degree')
        return value
