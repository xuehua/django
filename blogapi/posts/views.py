from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer, UserSerializer
# Create your views here.


class PostList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        if request.user.id == int(request.data['author']):
            #only allow users create their own posts.
            return super().post(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer