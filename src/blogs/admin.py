from django.contrib import admin

from blogs.models import Blog, Post, Categoria

admin.site.register(Categoria)
admin.site.register(Blog)
admin.site.register(Post)