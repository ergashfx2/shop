from django.urls import path
from .views import Order_Success

# urls.py
from django.urls import path

urlpatterns = [
    path('order/success/', Order_Success, name='order_success'),
]
