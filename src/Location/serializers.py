from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
 
 class Meta:
  model = Location
  fields = ('id', 'location_name', 'street_name', 'street_number', 'city', 'country')
  