from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_clubAdmin',
        'is_student', 'user_profile'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email','user_profile')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_clubAdmin', 'is_superuser','is_student',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email','user_profile')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_clubAdmin', 'is_superuser','is_student',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)