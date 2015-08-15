from django.contrib import admin

from products.models import Product, Stock, Warehouse


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    pass


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass
