from django.db import models

class Products(models.Model):
    product_id = models.PositiveSmallIntegerField()
    product_name = models.CharField(max_length= 20)
    product_image = models.ImageField()
    product_description = models.TextField()
    price = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.product_name}"




