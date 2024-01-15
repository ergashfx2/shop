from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from orders.models import Order
from products.models import Product
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductViewSet(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer


class DeleteProductApiView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


def get_response(serializer):
    return Response(serializer.data)


class UpdateProductAPiView(UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny, ]
    http_method_names = ['patch', 'put']
    queryset = Product.objects.all()

    def update(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = Product.objects.get(pk=product_id)
        serializer = self.get_serializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return get_response(serializer)


                                     # Order Api View


class OrdersViewSet(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


class CreateOrderApiView(CreateAPIView):
    queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer


class DeleteOrdertApiView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]


class UpdateOrderAPiView(UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny, ]
    http_method_names = ['patch', 'put']
    queryset = Order.objects.all()

    def update(self, request, *args, **kwargs):
        order_id = kwargs.get('pk')
        order = Order.objects.get(pk=order_id)
        serializer = self.get_serializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return get_response(serializer)