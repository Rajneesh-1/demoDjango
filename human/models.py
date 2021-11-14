from django.db import models

# Create your models here.
class DetailsOfHuman(models.Model):
    name = models.CharField(max_length=15)
    city = models.CharField(max_length=10)
    favourite_food = models.CharField(max_length=15)