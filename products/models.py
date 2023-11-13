from django.db import models

PRODUCT_TYPE_CHOICES = [
    ('ayollar', 'Ayollar'),
    ('erkaklar', 'Erkaklar'),
    ('bolalar', 'Bolalar'),
    ('uy-xojalik', "Uy-Xo'jalik"),
    ('salomatlik', "Salomatlik")
]


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES, default='none')

    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(upload_to='products/')  # You need to configure MEDIA_ROOT and MEDIA_URL in settings.py

    def __str__(self):
        return self.title
