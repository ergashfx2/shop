from django.shortcuts import render, redirect
from users.models import CustomUser
from products.models import Product
from orders.models import Order
from django.contrib import messages
from django.views.generic import CreateView
from .models import Order


def Order_Success(request):
    if request.user.is_authenticated:
        message = messages.success(request,"Buyurtmangiz muvaffaqiyatli qabul qilindi. Buyurtmangiz holatini buyurtmalarim bo'limidan kuzatib borishingiz mumkin")
        return render(request, template_name="order_success.html",context=message)
    else:
        message = messages.success(request,"Buyurtmangiz muvaffaqiyatli qabul qilindi. Buyurtmangiz holatini kuzatib borish uchun saytdan ro'yxatdan o'ting")
        return render(request, template_name="order_success.html",context=message)

