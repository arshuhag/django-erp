from django.contrib import admin

from .models import (
    Category,
    Product,
    Supplier,
    Warehouse,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'phone',
    )


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'location',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'sku',
        'price',
        'stock_quantity',
        'is_low_stock',
    )

    search_fields = (
        'name',
        'sku',
    )

    list_filter = (
        'category',
        'warehouse',
    )