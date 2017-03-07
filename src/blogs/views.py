from django.http import HttpResponse
from django.shortcuts import render

from blogs.forms import PostForm
from blogs.models import Blog, Post


def posts_list(request):
    """
    Recupera todos los blogs de la base de datos y los pinta.
    :param request: HttpRequest
    :return: HttpResponse
    """

    # recupera posts
    posts = Post.objects.all()

    # prepara el contexto de la plantilla
    context = {
        'post_objects': posts
    }

    # renderiza y devuelve la plantilla
    return render(request, 'blogs/inicio.html', context)


def blogs_list(request):
    """
    Recupera todos los blogs de la base de datos y los pinta.
    :param request: HttpRequest
    :return: HttpResponse
    """

    # recupera blogs
    blogs = Blog.objects.all()

    # prepara el contexto de la plantilla
    context = {
        'blog_objects': blogs
    }

    # renderiza y devuelve la plantilla
    return render(request, 'blogs/blogs.html', context)

def new_post(request):
    """
    Recupera todos los blogs de la base de datos y los pinta.
    :param request: HttpRequest
    :return: HttpResponse
    """

    # crear el formulario
    form = PostForm()

    # renderiza la plantilla con el formulario
    context = {
        "form": form
    }

    # renderiza y devuelve la plantilla
    return render(request, 'blogs/new-post.html', context)