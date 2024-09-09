from django.contrib import admin

from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by','slug', 'price', 'in_stock', 'created', 'updated']
    list_editable = ['in_stock', 'price']
    list_filter = ['is_active', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}