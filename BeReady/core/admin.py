from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import StudentWorkPost, NewsPost, StudentWorkDiscussion, NewsDiscussion, Lesson


@admin.register(StudentWorkPost)
class StudentWorkPost(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'owner', 'file')


@admin.register(NewsPost)
class NewsPost(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'owner', 'file')


@admin.register(StudentWorkDiscussion)
class StudentWorkDiscussion(admin.ModelAdmin):
    list_display = ('comment', 'date', 'owner', 'post')


@admin.register(NewsDiscussion)
class NewsDiscussion(admin.ModelAdmin):
    list_display = ('comment', 'date', 'owner', 'post')


@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ('name', 'subject', 'classCode', 'owner', 'students', 'faculty')
