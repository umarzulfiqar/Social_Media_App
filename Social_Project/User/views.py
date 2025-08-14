from django.shortcuts import render
from .models import UserProfile,Follow
from .serializers import UserProfileSerializer,UserProfileUpdateRetreveSerializer,FollowSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from Post.serializers import PostSerializer
from Post.models import Post


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
    
class Login(APIView):
    throttle_classes = [UserRateThrottle,AnonRateThrottle]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username , password=password)

        if user is not None:
            return Response({"message":"You logeg in sucessfully"}, status=status.HTTP_200_OK)
        
        return Response({"message":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
    
class UserProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileUpdateRetreveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user = self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user = self.request.user)


class FollowView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowSerializer
    
    def perform_create(self, serializer):
        follow_user = serializer.validated_data.get('following')
        follower_user = self.request.user

        if Follow.objects.filter(follow=follower_user, following=follow_user).exists():
            raise ValidationError({"detail": "Already following this user."})
        serializer.save(follow = self.request.user)

class UnFollowView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self,request , *args,**kwargs ):
        following_id = kwargs.get('user_id')
        follow = Follow.objects.filter(follow = request.user, following_id = following_id).first()
        if follow:
            follow.delete()
            return Response({"detail":"Unfollowed successfully"},status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)
    

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        followed_user = Follow.objects.filter(follow=self.request.user).values_list("following", flat=True)
        return Post.objects.filter(post_user__in = followed_user).order_by('-created_at')