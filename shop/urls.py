from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import users.urls
from users.views import HomePage
schema_view = get_schema_view(
    openapi.Info(
        title="Online Shop",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://ergashali001.pythonanywhere.com/",
        contact=openapi.Contact(email="ergashaliabduvohidov@gmail.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('', HomePage, name='home'),
    path('admin/', admin.site.urls),
    path('user/', auth_views.LoginView.as_view()),
    path('user/', include(users.urls)),
    path('product/', include('products.urls')),
    path('', include('orders.urls')),
    path('api/', include('api_app.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
