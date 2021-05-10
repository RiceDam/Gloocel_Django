from django.shortcuts import render
from .models import Door
from rest_framework import mixins
from rest_framework import generics
from .serializers import DoorSerializer

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


class DoorOpen(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer

    """
    Validates the user's session, then sends a message to the
    RabbitMQ message queue. 
    """
    def post(self, request, *args, **kwargs):
        # Validate user session

        
        # Send message to RabbitMQ


        # Returns a message to the user that the door has opened
        return 

    