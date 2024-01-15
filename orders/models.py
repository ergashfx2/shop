from django.db import models

from products.models import Product

StatusChoices = (
    ('Qabul qilindi', 'Qabul qilindi'),
    ('Bekor qilindi', 'Bekor qilindi'),
    ("Yetkazilmoqda", 'Yetkazilmoqda'),
    ('Yetkazib berildi', 'Yetkazib berildi'),
)

from users.models import Location_choices


# Create your models here.

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=StatusChoices, default="Qabul qilindi")
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=30)
    customer_location = models.CharField(max_length=200, choices=Location_choices)

    def save(self, *args, **kwargs):
        self.customer_phone = int(str(self.customer_phone).replace(" ", ""))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product
