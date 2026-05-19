from django.contrib import admin

from .models import (
    Department,
    Designation,
    Employee,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
    )


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        'employee_id',
        'user',
        'department',
        'designation',
        'salary',
    )

    search_fields = (
        'employee_id',
        'user__username',
    )

    list_filter = (
        'department',
        'designation',
    )