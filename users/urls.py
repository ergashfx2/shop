from django.urls import path
from .views import SignUp, SignIn, Password_Reset, HomePage,my_logout_view

urlpatterns = [
    path('signup/', SignUp, name='signup'),
    path('', HomePage, name='home'),
    path('signin', SignIn, name='signin'),
    path('logout/', my_logout_view, name='logout'),
    path('password-reset', Password_Reset, name='password-reset')
]
