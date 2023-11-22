from django.contrib import admin
from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['title', 'price', 'image','description','type']


admin.site.register(Product, ProductAdmin)



