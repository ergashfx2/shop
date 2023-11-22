from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'age','phone','image', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
