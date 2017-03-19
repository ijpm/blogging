# -*- coding: utf-8 -*-
from rest_framework import serializers

from blogs.models import Blog, Post


class BlogListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'name', 'tematica', 'owner')

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'name', 'tematica')


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'titulo', 'introduccion', 'cuerpo', 'publish_at', 'state', 'url', 'owner', 'categorias')

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'titulo', 'owner', 'categorias')