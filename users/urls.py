from django.urls import path
from .views import SignUp, SignIn, Password_Reset, HomePage, my_logout_view, Profile

urlpatterns = [
    path('signup/', SignUp, name='signup'),
    path('signin/', SignIn, name='signin'),
    path('profile/', Profile, name='profile'),
    path('logout/', my_logout_view, name='logout'),
    path('password-reset/', Password_Reset, name='password-reset')
]
