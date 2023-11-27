from django.contrib import admin

from .models import Product
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class ProductAdmin(SummernoteModelAdmin):
    model = Product
    list_display = ['title', 'price', 'image', 'description', 'type']
    summernote_fields = ('description')


admin.site.register(Product, ProductAdmin)
