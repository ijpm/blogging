# -*- coding: utf-8 -*-
from rest_framework import serializers

from blogs.models import Blog

class BlogListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'name', 'tematica')

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'