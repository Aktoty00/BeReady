from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser, Teacher, Student


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'username', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'role', 'status', 'student')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username', 'role', 'age')
