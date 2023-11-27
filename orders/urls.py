from django.urls import path
from .views import Order_Success,EditOrder, DeleteOrder
from django.urls import path

urlpatterns = [
    path('order/success/<int:pk>/', Order_Success, name='order_success'),
    path('order/edit/<int:pk>/', EditOrder, name='edit_order'),
    path('order/delete/<int:pk>/', DeleteOrder, name='delete_order'),
]
