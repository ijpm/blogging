# -*- coding: utf-8 -*-
from rest_framework.filters import SearchFilter, OrderingFilter, DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog, Post
from blogs.permissions import PostPermission
from blogs.serializers import BlogSerializer, BlogListSerializer, PostSerializer, PostListSerializer, BlogPostSerializer


class IsOwnerOrReadOnly(object):
    pass


class BlogViewSet(ModelViewSet):

    permission_classes = (IsAuthenticated, PostPermission)
    queryset = Blog.objects.all()
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ("name", "description")
    ordering_fields = ("name", "owner", "created_at")
    filter_fields = ("name", "owner", "created_at")

    def get_serializer_class(self):
        return BlogListSerializer if self.action == "list" else BlogSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostViewSet(ModelViewSet):

    permission_classes = (PostPermission, IsAuthenticated)
    queryset = Post.objects.order_by('-publish_at').all()
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('titulo','cuerpo')
    ordering_fields = ('publish_at', 'titulo')

    def get_serializer_class(self):
        return PostListSerializer if self.action == "list" else PostSerializer