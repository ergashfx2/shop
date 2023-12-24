from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import users.urls
from users.views import HomePage

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('', HomePage, name='home'),
    path('admin/', admin.site.urls),
    path('user/', auth_views.LoginView.as_view()),
    path('user/', include(users.urls)),
    path('product/', include('products.urls')),
    path('', include('orders.urls')),
    path('', include('api.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
