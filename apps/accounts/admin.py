from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'id',
        'username',
        'email',
        'role',
        'is_staff',
        'is_active',
    )
    
    list_display_links = (
        'username',
    )

    list_filter = (
        'role',
        'is_staff',
        'is_active',
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            'ERP Information',
            {
                'fields': (
                    'role',
                    'phone',
                    'profile_image',
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'ERP Information',
            {
                'fields': (
                    'role',
                    'phone',
                    'profile_image',
                )
            },
        ),
    )