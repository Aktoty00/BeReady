# from rest_framework import serializers
#
# from .models import Student, Teacher, MyUser
# # from ..core.serializers import ClassShortSerializer, ClassLongSerializer
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyUser
#         fields = ('first_name', 'last_name', 'email')
#
#     def validate(self, attrs):
#         return attrs
#
#
# class StudentSerializer(UserSerializer):
#     role = serializers.CharField(required=True)
#     age = serializers.IntegerField()
#     # classes = ClassShortSerializer(many=True)
#
#     class Meta(UserSerializer.Meta):
#         fields = UserSerializer.Meta.fields + ('role', 'age', 'classes')
#
#
# class TeacherSerializer(UserSerializer):
#     role = serializers.CharField(required=True)
#     status = serializers.CharField()
#     student = StudentSerializer(many=True)
#     # classes = ClassLongSerializer(many=True)
#
#     class Meta(UserSerializer.Meta):
#         fields = UserSerializer.Meta.fields + ('role', 'status', 'student', 'classes')
#
