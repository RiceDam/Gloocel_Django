from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Person

# class RegisterSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Person
#         fields = ('__all__')

class PersonSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        person = Person.objects.create_user(**validated_data)
        return person

    class Meta:
        model = Person

        fields = (
            'user.username',
            'first_name',
            'last_name',
            'email',
            'user.password',
        )

        validators = [
            UniqueTogetherValidator(
                queryset = Person.objects.all(),
                fields = ['user.username', 'email']
            )
        ]
