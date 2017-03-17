# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import Blog
from blogs.serializers import BlogSerializer


class BlogAPI(APIView):
    """
    List (GET)
    """
    def get(self, request):
        """
        Devuelve lista de blogs
        :param request:
        :return:
        """
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
