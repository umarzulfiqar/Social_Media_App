from rest_framework import serializers
from .models import Post,Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['created_at','post_user']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields= ['created_at','user','post']

        def create(self,validated_data):        #It will get current loged in user
            request = self.context['request']
            validated_data['user'] = request.user
            return super().create(validated_data)