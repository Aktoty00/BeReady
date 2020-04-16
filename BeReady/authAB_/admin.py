from django.contrib import admin

from .models import Teacher, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')


@admin.register(Student)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
