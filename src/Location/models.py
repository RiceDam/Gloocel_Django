from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length = 50, null = True)
    street_name = models.CharField(max_length=100, null= True)
    street_number = models.CharField(max_length=100, null= True)
    city = models.CharField(max_length=100, null= True)
    country = models.CharField(max_length=100, null= True)