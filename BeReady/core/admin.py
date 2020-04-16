from django.contrib import admin

from .models import StudentWorkPost, NewsPost, NewsDiscussion, Lesson, \
    StudentWorkDiscussion


@admin.register(StudentWorkPost)
class StudentWorkPost(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'owner', 'file')


@admin.register(NewsPost)
class NewsPost(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'owner', 'file')


@admin.register(StudentWorkDiscussion)
class StudentWorkDiscussion(admin.ModelAdmin):
    list_display = ('comment', 'date', 'owner', 'post', 'sendTo')


@admin.register(NewsDiscussion)
class NewsDiscussion(admin.ModelAdmin):
    list_display = ('comment', 'date', 'owner', 'post')


@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ('name', 'subject', 'classCode', 'owner', 'students')
