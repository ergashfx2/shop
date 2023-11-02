from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=False)
    password = models.CharField(max_length=10)
    phone = models.CharField(max_length=15, null=True)

