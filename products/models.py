from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')  # You need to configure MEDIA_ROOT and MEDIA_URL in settings.py

    def __str__(self):
        return self.title
