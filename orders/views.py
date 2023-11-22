from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser
from products.models import Product
from orders.models import Order
from django.contrib import messages
from django.views.generic import CreateView

from .forms import EditOrderForm
from .models import Order


def Order_Success(request):
    if request.user.is_authenticated:
        message = messages.success(request,
                                   "Buyurtmangiz muvaffaqiyatli qabul qilindi. Buyurtmangiz holatini buyurtmalarim bo'limidan kuzatib borishingiz mumkin")
        return render(request, template_name="order/order_success.html", context=message)
    else:
        message = messages.success(request,
                                   "Buyurtmangiz muvaffaqiyatli qabul qilindi. Buyurtmangiz holatini kuzatib borish uchun saytdan ro'yxatdan o'ting")
        return render(request, template_name="order/order_success.html", context=message)


def EditOrder(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        form = EditOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditOrderForm(instance=order)

    return render(request, 'admin/edit_order.html', {'form': form, 'order': order})


def DeleteOrder(request,pk):
    order = get_object_or_404(Order,pk=pk)
    if request.method == "POST":
        order.delete()
        messages.success(request,message="Buyurtma muvaffaqiyatli bekor qilindi")
        return redirect('orders')
    orders = {
        'order' : order
    }
    return render(request, template_name="admin/delete_order.html", context=orders)