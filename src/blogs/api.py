# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import Blog
from blogs.serializers import BlogSerializer, BlogListSerializer


class BlogAPI(ListCreateAPIView):
    """
    List (GET)
    """
    queryset = Blog.objects.all()

    def get_serializer_class(self):
        return BlogListSerializer if self.request.method == 'GET' else BlogSerializer

class BlogDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    detalle, actualizacion y borrado de blogs
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer