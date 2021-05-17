from django.http import Http404
from django.shortcuts import render
from .models import Door
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DoorSerializer
import json
import pika
from datetime import datetime

class DoorList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
 queryset = Door.objects.all()
 serializer_class = DoorSerializer

 """
 Returns a list of all doors

 TODO
 Only return doors that the user has access to
 """
 def get(self, request, *args, **kwargs):
  return self.list(request, *args, **kwargs)


class DoorOpen(APIView):

 connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
 channel = connection.channel()
 channel.confirm_delivery()
 """
 Get an instance of the Door from the database
 """

 def load_queue(self, door):
  try:

   now = datetime.now()
   dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
   message = "OPEN DOOR Message sent: {}".format(dt_string)

   self.channel.basic_publish(exchange='',
   routing_key=door.door_name,
   body=message, mandatory=True)

   return json.dumps({
    'success': 'Added a message request to ' + door.door_name + ' ' + message
   })
  except Exception as e:
   return json.dumps({
    'error': str(e)
   }) 

 def get_door(self, pk):
  try:
   return Door.objects.get(pk=pk)
  except Door.DoesNotExist:
   raise Http404

 def post(self, request, pk, format=None):
  door = self.get_door(pk)
  response = self.load_queue(door)
  return Response(response)
