from django.shortcuts import render
from rest_framework import generics
from .models import User, Todos, Photo, Album, Post, Comment
from .serializers import UserSerializer, TodosSerializer, PhotoSerializer, AlbumSerializer, PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
# Create your views here.


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SinglePost(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SinglePostComments(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(postId=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentFilterView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        postId = self.request.query_params.get('postId')
        if postId is not None:
            queryset = queryset.filter(postId=postId)
        return queryset


class PostGenerator(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

class AlbumGenerator(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

class AlbumList(APIView):
    def get(self, request, format=None):
        album = Album.objects.all()
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data)


class PhotoGenerator(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

class PhotoList(APIView):
    def get(self, request, format=None):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

class TodoGenerator(generics.ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

class TodoList(APIView):
    def get(self, request, format=None):
        todos = Todos.objects.all()
        serializer = TodosSerializer(todos, many=True)
        return Response(serializer.data)

class UserGenerator(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)