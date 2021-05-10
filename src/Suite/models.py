from django.db import models
from location.models import Location

# Create your models here.
class Suite(models.Model):
    suite_number = models.CharField(max_length=255)
    version = models.IntegerField()
    location = models.ForeignKey(Location, related_name='Location_Suite', null=True, on_delete=models.CASCADE)



