# -*- coding: utf-8 -*-
from rest_framework.filters import SearchFilter, OrderingFilter, DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog, Post
from blogs.permissions import PostPermission
from blogs.serializers import BlogSerializer, BlogListSerializer, PostSerializer, PostListSerializer, BlogPostSerializer


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
    search_fields = ('titulo','cuerpo')
    ordering_fields = ('publish_at', 'titulo')

    def get_serializer_class(self):
        return PostListSerializer if self.action == "list" else PostSerializer

class BlogPostAPI(APIView):
    """
    List (GET)
    """
    def get(self, request, pk):
        """
        Devuelve lista de blogs
        :param request:
        :return:
        """

        blog = get_object_or_404(Blog, id=pk)

        if request.user.is_authenticated():
            if request.user.is_superuser or request.user == blog.owner:
                posts = Post.objects.order_by('-publish_at').filter(owner=blog.id)
            else:
                posts = Post.objects.order_by('-publish_at').filter(owner=blog.id,state="PUB")
        else:
            posts = Post.objects.order_by('-publish_at').filter(owner=blog.id, state="PUB")

        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)