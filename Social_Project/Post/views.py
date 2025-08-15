from rest_framework.views import APIView
from rest_framework import permissions
from .models import Post,Comment,Like
from rest_framework import status
from .serializers import PostSerializer,CommentSerializer,LikeSerialier
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework import generics


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
    

class CommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['id']
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')
    
    def perform_create(self, serializer):
        post_id = self.kwargs['id']
        serializer.save(user= self.request.user, post_id = post_id)

class CommentDeleteView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(user = self.request.user)
    
class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk):
        post = get_object_or_404(Post,id=pk)
        like = Like.objects.filter(post=post, user = request.user)    #unlike
        if like.exists():
            like.delete()
            return Response({"message":"Unliked Successfully","Total likes":post.likes.count()},status=status.HTTP_200_OK)
        else:                                                         #like
            Like.objects.create(post=post, user = request.user)
            return Response({"message":"Liked Successfully","Total likes":post.likes.count()},status=status.HTTP_200_OK)
        