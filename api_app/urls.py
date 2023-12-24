from django.urls import path
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Product', ProductViewSet, basename='products')

urlpatterns = router.urls
