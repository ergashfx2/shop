from django.db import models


# Create your models here.

class Notifications(models.Model):
    title = models.CharField(max_length=300)
    body = models.CharField(max_length=2000)
