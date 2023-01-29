from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'rating', 'count',  'date']


admin.site.register(Product, ProductAdmin)
