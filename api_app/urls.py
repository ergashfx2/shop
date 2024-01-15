from django.urls import path
from django.views.generic import TemplateView

from .views import ProductViewSet, CreateProductView, DeleteProductApiView, UpdateProductAPiView, OrdersViewSet,CreateOrderApiView,DeleteOrdertApiView,UpdateOrderAPiView

urlpatterns = [
    path("redoc/",TemplateView.as_view(template_name="redoc.html", extra_context={"schema_url": "openapi-schema"}),name="redoc",),
    path('all/', ProductViewSet.as_view(), name='all'),
    path('create-product/', CreateProductView.as_view(), name="product-create'"),
    path('delete/<int:pk>/', DeleteProductApiView.as_view()),
    path('update/<int:pk>/', UpdateProductAPiView.as_view()),
    path('orders/all/', OrdersViewSet.as_view()),
    path('create-order/', CreateOrderApiView.as_view(), name="product-create'"),
    path('order/delete/<int:pk>/', DeleteOrdertApiView.as_view()),
    path('order/update/<int:pk>/', UpdateOrderAPiView.as_view()),
]
