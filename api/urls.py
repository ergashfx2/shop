# api/urls.py
from django.urls import path, include

urlpatterns = [
    path('api/', include('api_app.urls')),
    # Add other URL patterns as needed
]
