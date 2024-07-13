from django.db import models

class Ussd(models.Model):
    artisan_id = models.PositiveSmallIntegerField()
    artisan_phone_number = models.PositiveBigIntegerField()
    artisan_name = models.CharField()
    material = models.CharField()
    number_of_materials = models.PositiveIntegerField()
    kilograms= models.PositiveIntegerField()
    def __str__(self):
        return f"{self.artisan_phone_number}"
