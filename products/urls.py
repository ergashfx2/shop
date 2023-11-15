from django.urls import path
from .views import ProductDetail,ProductFilter,Edit_Product,Add_Product

urlpatterns = [
    path('<int:pk>/', ProductDetail, name='product_detail'),
    path('edit/<int:pk>', Edit_Product, name='edit_product'),
    path('create/', Add_Product, name='add_product'),
    path('products/<str:category>/', ProductFilter, name='product_filters'),

]
