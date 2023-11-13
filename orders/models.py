from django.db import models


# Create your models here.

class Order(models.Model):
    product = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    customer_location = models.CharField(max_length=200)
