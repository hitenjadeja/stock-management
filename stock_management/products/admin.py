from django.contrib import admin

from products.models import Product, Warehouse


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    pass
