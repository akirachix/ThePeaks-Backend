from customers import models
from customers.models import Customers
from product.models import Products

class Orders(models.Model):
    order_id = models.PositiveSmallIntegerField()
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_date = models.DateField()
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f"{self.order_id}"
