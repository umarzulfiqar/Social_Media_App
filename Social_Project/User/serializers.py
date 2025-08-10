from rest_framework import serializers
from .models import UserProfile,Follow

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"  

class UserProfileUpdateRetreveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar','bio']
        read_only_fileds = ['user']

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"
        read_only_fields = ['follow', 'created_at']

    def validate_following(self,value):
        request = self.context['request']
        if request.user == value:
            raise serializers.ValidationError("You cannot follow yourself.")
        return value