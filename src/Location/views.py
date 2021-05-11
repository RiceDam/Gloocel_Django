from .models import Location
from .serializers import LocationSerializer
from rest_framework import mixins
from rest_framework import generics 

# Create your views here.

class LocationList(
 mixins.ListModelMixin,
 mixins.CreateModelMixin,
 generics.GenericAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

  def get(self, request, *args, **kwargs):
   return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
   return self.create(request, *args, **kwargs)

class LocationDetail(
 mixins.RetrieveModelMixin,
 mixins.UpdateModelMixin,
 mixins.DestroyModelMixin,
 generics.GenericAPIView):
  
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

  def get(self, request, *args, **kwargs):
   return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
   return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
   return self.destroy(request, *args, **kwargs)


