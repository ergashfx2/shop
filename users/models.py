from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=False)
    phone = PhoneField(blank=True, help_text='Raqamingizni kiritish')

    def __str__(self):
        return self.username
