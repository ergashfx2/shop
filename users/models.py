from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.db import models

Location_choices = (
    ('choice', 'Manzilni tanlash'),
    ('toshkent', 'Toshkent Shahri'),
    ('andijon', 'Andijon Viloyati'),
    ('buxoro', 'Buxoro Viloyati'),
    ('fargona', "Farg'ona Viloyati"),
    ('jizzax', "Jizzax Viloyati"),
    ('qoraqalpogiston', "Qoraqalpog'iston Respublikasi"),
    ('namangan', "Namangan Viloyati"),
    ('navoiy', "Navoiy Viloyati"),
    ('samarqand', "Samarqand Viloyati"),
    ('surxondaryo', "Surxondaryo Viloyati"),
    ('toshkent_viloyati', "Toshkent Viloyati"),
    ('xorazm', "Xorazm Viloyati"),
)


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=False)
    password = models.CharField(max_length=10)
    phone = models.IntegerField( null=True)
    image = models.ImageField(upload_to='users/',blank=True, null=True)
    location = models.CharField(max_length=255, choices=Location_choices,default=None)
