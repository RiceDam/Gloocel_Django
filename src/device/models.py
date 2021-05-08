from django.db import models
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.models import AbstractAPIKey

# Create your models here.

class Device(models.Model):

  """
  def key_default(myName):
    api_key, key = APIKey.objects.create_key(name=myName)
    return key
  """

  def api_key_create(device):
    device_api_key = DeviceAPIKey.create_device_key(device=device)
    print(device_api_key)
  
  device_name = models.CharField(max_length=255, primary_key=True)
  device_type = models.CharField(max_length=30)
  #api_key = models.CharField(max_length=255, blank=True, null=True, editable=False)


  def save(self, *args, **kwargs):
    #self.api_key = Device.key_default(self.device_name)
    Device.api_key_create(self)
    super().save(*args, **kwargs)
    """
      TODO: 
        Create a message queue when a device is created
        API endpoint on the backend server will allow a device to poll
        if this message queue has any messages, if there is a message
        the message will be extracted from the message queue
    """
    # createMessageQueue(self.device_name)


  def delete(self, *args, **kwargs):
    #self.api_key = Device.key_default(self.device_name)
    super().save(*args, **kwargs)
    """
      TODO: 
        Create a message queue when a device is created
        API endpoint on the backend server will allow a device to poll
        if this message queue has any messages, if there is a message
        the message will be extracted from the message queue
    """
    # createMessageQueue(self.device_name)


class DeviceAPIKey(AbstractAPIKey):

  def __init__(self, device, name):
    super().__init__(device=device,name=name)

  @classmethod
  def create_device_key(cls,device):
    name = device.device_name
    print("NAME", device.device_name)
    device_api_key = cls(device=device, name=name)
    device_api_key.set_name("bob")
    device_api_key.save()
    return device_api_key
  
  def set_name(self, name):
    print(self)
    self.name = name

  device = models.ForeignKey(
    Device,
    on_delete=models.CASCADE,
    related_name="api_keys",
    null=True
  )
