from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework import generics

from .models import Post
from .serializers import PostBaseModelSerializer, PostListModelSerializer, PostCreateModelSerializer,PostRetrieveModelSerializer
# Create your views here.

#게시글 목록 + 생성
class PostListCreateView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

#게시글 디테일 , 수정, 삭제
class PostRetrieveView(generics.RetrieveAPIView, generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveModelSerializer



class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer
