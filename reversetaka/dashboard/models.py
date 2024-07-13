from django.db import models
class Dashboard(models.Model):
    user_id = models.PositiveSmallIntegerField()
    user_first_name = models.CharField()
    user_last_name = models.CharField()
    user_email = models.EmailField()
    def __str__(self):
        return f"{self.user_first_name}"
