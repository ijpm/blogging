# -*- coding: utf-8 -*-
from rest_framework.filters import SearchFilter, OrderingFilter, DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog, Post
from blogs.permissions import PostPermission
from blogs.serializers import BlogSerializer, BlogListSerializer, PostSerializer, PostListSerializer


class BlogViewSet(ModelViewSet):

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

    permission_classes = (PostPermission,)
    queryset = Post.objects.order_by('-publish_at').all()
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('titulo', 'introduccion', 'cuerpo', 'categorias')
    ordering_fields = ('publish_at', 'state', 'owner', 'categorias')
    filter_fields = ('state', 'owner', 'categorias')

    def get_serializer_class(self):
        return PostListSerializer if self.action == "list" else PostSerializer