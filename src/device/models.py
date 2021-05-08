from django.db import models
from rest_framework_api_key.models import APIKey
# Create your models here.

class Device(models.Model, ):

  def key_default():
    return "1234678"


  device_name = models.CharField(max_length=255, primary_key=True)
  device_type = models.CharField(max_length=30)
  api_key = models.CharField(max_length=255, default=key_default, editable=False)


  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    """
      TODO: 
        Create a message queue when a device is created
        API endpoint on the backend server will allow a device to poll
        if this message queue has any messages, if there is a message
        the message will be extracted from the message queue
    """
    # createMessageQueue(self.device_name)

