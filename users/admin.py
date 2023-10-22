from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
<<<<<<< HEAD
=======
from .forms import CustomUserCreationForm, CustomUserChangeForm
>>>>>>> 1aab88a (Initial commit)
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
<<<<<<< HEAD
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name','location', 'age','phone','image', 'is_staff']
=======
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'age','phone', 'is_staff']
>>>>>>> 1aab88a (Initial commit)


admin.site.register(CustomUser, CustomUserAdmin)
