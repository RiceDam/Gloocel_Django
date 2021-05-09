from django.db import models

# Create your models here.
class Door(models.Model):
    door_name = models.CharField(max_length = 50, null = True)
    door_type = models.CharField(max_length = 30)
    # location_id = models.ForeignKey(Location, on_delete=models.CASCADE)