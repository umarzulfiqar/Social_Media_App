from rest_framework.views import APIView
from rest_framework import permissions
from .models import Post
from rest_framework import status
from .serializers import PostSerializer
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404



class PostListCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(post_user = request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        posts= Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class PostDetail(APIView):
    permission_classes=[permissions.IsAuthenticated,IsOwnerOrReadOnly]

    def get_object(self, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(self.request, post)
        return post
    
    def get(self, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self,request,pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post,data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)