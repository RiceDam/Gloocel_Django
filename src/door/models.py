from django.db import models
from location.models import Location
from django.db.models.signals import pre_save
import pika 

# Create your models here.
class Door(models.Model):
 door_name = models.CharField(max_length = 50, null= True, unique=True)
 door_type = models.CharField(max_length = 30)
 location = models.ForeignKey(Location, related_name='Location_Door', null=True, on_delete=models.CASCADE)
 message = models.CharField(max_length=255, editable=False, default=None, blank=True, null=True)

 def __str__(self):
  return self.door_name + ' | ' + str(self.location)

# when model is created calls rabbitmq create queue function 
def create_queue(sender, instance, **kwargs):
  print("Done saving an instance now creating a queue")
  # Change this for production
  connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
  channel = connection.channel()
  msg_table = channel.queue_declare(queue=instance.door_name)
  instance.message = msg_table

pre_save.connect(create_queue, sender=Door)



