from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'username', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )
