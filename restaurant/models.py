from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.SmallIntegerField()
    date = models.DateField(auto_now_add=True)