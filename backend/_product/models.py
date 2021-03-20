from django.db import models

from backend._order import models as order_models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    order = models.ForeignKey(
        order_models.Order,
        on_delete=models.CASCADE,
        related_name="products")
