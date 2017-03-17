from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from django.views.generic.list import ListView
from django.utils import timezone

from blogs.forms import PostForm, BlogForm
from blogs.models import Blog, Post, Categoria


def posts_list(request):
    """
    Recupera todos los blogs de la base de datos y los pinta.
    :param request: HttpRequest
    :return: HttpResponse
    """

    # recupera posts
    posts = Post.objects.select_related("owner").all()
    categorias = Categoria.objects.all()

    # prepara el contexto de la plantilla
    context = {
        'post_objects': posts,
        'categoria_objects': categorias
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

class NewPostView(View):

    @method_decorator(login_required)
    def get(self, request):
        """
        Sireve el formulario de crear post al usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

        # crear el formulario
        form = PostForm()
        form.fields['owner'].queryset = Blog.objects.filter(owner=request.user)
        # renderiza la plantilla con el formulario
        context = {
            "form": form
        }

        # renderiza y devuelve la plantilla
        return render(request, 'blogs/new-post.html', context)

    @method_decorator(login_required)
    def post(self, request):
        """
        Recibe los datos del nuevo post los valida y los guarda
        :param request: HttpRequest
        :return: HttpResponse        """

        # crear el formulario con los datos del post
        form = PostForm(request.POST)

        if form.is_valid():
            #crea el post
            post = form.save()

            #generar mensaje de exito
            msg = "Post creado con éxito"
            form = PostForm()
        else:
            msg = "Ha ocurrido un error al guardar el post" \


        # renderiza la plantilla con el formulario
        context = {
            "form": form,
            "msg": msg
        }

        # renderiza y devuelve la plantilla
        return render(request, 'blogs/new-post.html', context)

class NewBlogView(View):

    @method_decorator(login_required)
    def get(self, request):
        """
        Sireve el formulario de crear post al usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

        # crear el formulario
        form = BlogForm()

        # renderiza la plantilla con el formulario
        context = {
            "form": form
        }

        # renderiza y devuelve la plantilla
        return render(request, 'blogs/new-blog.html', context)

    @method_decorator(login_required)
    def post(self, request):
        """
        Recibe los datos del nuevo post los valida y los guarda
        :param request: HttpRequest
        :return: HttpResponse        """

        # crear el formulario con los datos del POST
        blog_with_user = Blog(owner=request.user)
        form = BlogForm(request.POST, instance=blog_with_user)

        if form.is_valid():
            #crea el post
            blog = form.save()

            #generar mensaje de exito
            msg = "Blog creado con éxito"
            # limpiamos el formulario creando uno vacío para pasar a la plantilla
            form = BlogForm()
        else:
            msg = "Ha ocurrido un error al guardar el blog" \


        # renderiza la plantilla con el formulario
        context = {
            "form": form,
            "msg": msg
        }

        # renderiza y devuelve la plantilla
        return render(request, 'blogs/new-blog.html', context)

class PostListView(View):

    @method_decorator(login_required)
    def get(self, request):
        """
        Sireve el formulario de crear post al usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

        # recupera posts
        posts = Post.objects.filter(owner__in=request.user.owned_blogs.all())

        # prepara el contexto de la plantilla
        context = {
            'post_objects': posts
        }

        # renderiza y devuelve la plantilla
        return render(request, 'blogs/inicio.html', context)

class BlogListView(View):

    @method_decorator(login_required)
    def get(self, request):
        """
        Sireve el formulario de crear post al usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

        # recupera blogs
        blogs = Blog.objects.filter(owner=request.user)

        # prepara el contexto de la plantilla
        context = {
            'blog_objects': blogs,
        'pon_nombre': 'ponloponlo'
        }

        # renderiza y devuelve la plantilla
        return render(request, 'blogs/blogs.html', context)

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