from django.db import models

StatusChoices = (
    ('Qabul qilindi', 'Qabul qilindi'),
    ('Bekor qilindi', 'Bekor qilindi'),
    ("Yetkazilmoqda", 'Yetkazilmoqda'),
    ('Yetkazib berildi', 'Yetkazib berildi'),
)

from users.models import Location_choices


# Create your models here.

class Order(models.Model):
    product = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=StatusChoices, default="Qabul qilindi")
    customer_name = models.CharField(max_length=200)
    customer_phone = models.IntegerField()
    customer_location = models.CharField(max_length=200, choices=Location_choices)
