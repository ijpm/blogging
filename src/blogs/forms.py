# -*- coding: utf-8 -*-
from django import forms

from blogs.models import Post, Blog

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["titulo", "introduccion", "cuerpo", "publish_at", "url", "owner", "categorias"]

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ["name", "description", "tematica"]