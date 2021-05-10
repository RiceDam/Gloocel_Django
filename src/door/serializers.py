from rest_framework import serializers
from .models import Door

class DoorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Door
        fields = ('door_name', 'door_type')
        # fields = ('door_name', 'door_type', 'location_id')
