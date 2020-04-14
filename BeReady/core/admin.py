from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Discussion, Post, Class


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'discussion', 'file')


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'classCode', 'subject', 'post')
