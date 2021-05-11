from django.http import Http404
from django.shortcuts import render
import json
from .models import Door
from rest_framework import mixins
from rest_framework import generics
from .serializers import DoorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class DoorList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer

    """
    TODO

    User sends their session id and we convert it to their
    user id. Afterwards, we verify and send a response with
    the doors the user has access to.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DoorOpen(APIView):
 """
 Get an instance of the Door from the database
 """

 def load_queue(self, door):
  try:
   #TODO: Instead of printing here add code to load the Door's message queue
   # Will need to retrieve the device associated with the Door, 
   # so need some relationship between the door and the device

   print("Mocking loading a message into RabbitMQ Queue")
   return json.dumps({
    'success': 'Added a message request to ' + door.door_name
   })
  except Exception as e:
   return json.dumps({
    'error': e.message
   }) 

 def get_door(self, pk):
  try:
   return Door.objects.get(pk=pk)
  except Door.DoesNotExist:
   raise Http404

 def get(self, request, pk, format=None):
  door = self.get_door(pk)
  response = self.load_queue(door)
  return Response(response)