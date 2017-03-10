# -*- coding: utf-8 -*-
from django import forms

from blogs.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["titulo", "introduccion", "cuerpo", "publish_at", "url", "owner", "categoria"]