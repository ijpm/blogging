from django.contrib.auth.decorators import login_required
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
    posts = Post.objects.select_related("owner").all()

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
    blogs = Blog.objects.select_related("owner").all()

    # prepara el contexto de la plantilla
    context = {
        'blog_objects': blogs
    }

    # renderiza y devuelve la plantilla
    return render(request, 'blogs/blogs.html', context)

@login_required()
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

def post_detail(request, post_pk):
    """
       Recupera una tarea de la base de datos y la pinta con una plantilla
       :param request: HttpRequest
       :param post_pk: Primary key del post a recuperar
       :return: HttpResponse
       """
    # recuperar el post
    try:
        post = Post.objects.select_related().get(pk=post_pk)
    except Post.DoesNotExist:
        return render(request, '404.html', {}, status=404)
    except Post.MultipleObjectsReturned:
        return HttpResponse("Existen varios posts con ese identificador", status=300)

    # preparar el contexto
    context = {
        'post': post
    }

    # renderizar la plantilla

    return render(request, 'blogs/post-detail.html', context)