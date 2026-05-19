from django.contrib import admin

from .models import (
    Customer,
    Order,
    OrderItem,
)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'phone',
    )

    search_fields = (
        'name',
        'phone',
    )


class OrderItemInline(admin.TabularInline):

    model = OrderItem

    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'customer',
        'payment_status',
        'total_amount',
        'order_date',
    )

    list_filter = (
        'payment_status',
    )

    inlines = [OrderItemInline]