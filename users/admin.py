from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name','location', 'age','phone','image', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
