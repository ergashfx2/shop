from django.urls import path
from .views import SignUp, SignIn, Password_Reset, HomePage, my_logout_view, Profile, MyOrders, EditProfile, About, \
    Settings, Contact
from notifications.views import Create_Notification, NotificationList

urlpatterns = [
    path('signup/', SignUp, name='signup'),
    path('signin/', SignIn, name='signin'),
    path('notifications/', NotificationList, name='notifications'),
    path('notification/create/', Create_Notification, name='create_notification'),
    path('profile/', Profile, name='profile'),
    path('settings/', Settings, name='settings'),
    path('profile/edit', EditProfile, name='edit_profile'),
    path('orders/', MyOrders, name='orders'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('logout/', my_logout_view, name='logout'),
    path('password-reset/', Password_Reset, name='password-reset')
]
