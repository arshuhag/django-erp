from django.contrib import admin

from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'action',
        'model_name',
        'object_id',
        'timestamp',
    )

    search_fields = (
        'model_name',
        'description',
    )

    list_filter = (
        'action',
        'model_name',
    )

    readonly_fields = (
        'user',
        'action',
        'model_name',
        'object_id',
        'description',
        'timestamp',
    )