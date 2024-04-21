from django.contrib import admin

from .models import Product, ProductImages, Category


class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ("name", "manufacturer", "voltage_level", "price", "created_on")
    list_filter = ("category", "voltage_level", "manufacturer", "phases")


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("name",)
