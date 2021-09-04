from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    price = models.IntegerField(blank=True, default=0)
