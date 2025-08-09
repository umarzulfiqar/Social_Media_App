from django.shortcuts import render
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status

class RegisterUser(APIView):
    def post(self,request):
        user_data = request.data
        #Create User in Django User
        user = User.objects.create_user(
            username=user_data.get("username"),
            password=user_data.get("password"),
            email=user_data.get("email")
        )
        #Create profile for that user
        profile = UserProfileSerializer(data={
            "user": user.id,
            "avatar": user_data.get("avatar"),
            "bio": user_data.get("bio")
        })
        if profile.is_valid():
            profile.save()
            return Response(profile.data, status=status.HTTP_201_CREATED)
        
        return Response(profile.errors, status=status.HTTP_400_BAD_REQUEST)