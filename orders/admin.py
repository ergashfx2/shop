from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['product', 'customer_name', 'customer_phone','customer_location','status']


admin.site.register(Order, OrderAdmin)