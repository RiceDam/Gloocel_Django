from django.shortcuts import render, redirect
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import PersonSerializer
from .models import Person

# Create your views here.

"""
Registers a user if they are (Haven't tested, don't know how
to format the JSON on postman)
"""
class RegisterAPI(generics.GenericAPIView):
    # Checks if the user.is_staff before allowing them to 
    # create an account
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = PersonSerializer(data = request.data)

        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                'error': True,
                'error_msg': serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

"""
Logs a user out and deletes their token from the database
"""
class LogoutAPI(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
