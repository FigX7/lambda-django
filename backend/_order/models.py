from django.db import models

from backend._customer import models as customer_models


class Order(models.Model):

    customer = models.ForeignKey(
        customer_models.Customer,
        related_name='orders',
        on_delete=models.CASCADE)
    date_order_placed = models.DateTimeField()
    quantity = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.id
