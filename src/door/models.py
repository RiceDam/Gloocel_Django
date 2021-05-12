from django.db import models
from location.models import Location

# Create your models here.
class Door(models.Model):
 door_name = models.CharField(max_length = 50, null= True)
 door_type = models.CharField(max_length = 30)
 location = models.ForeignKey(Location, related_name='Location_Door', null=True, on_delete=models.CASCADE)

 def __str__(self):
  return self.door_name + ' | ' + str(self.location)
