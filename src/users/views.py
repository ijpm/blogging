from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from users.forms import LoginForm, UserCreationForm


class LoginView(View):

    def get(self, request):
        """
        Presenta el formulario de login a un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        context = {
            'form': LoginForm()
        }

        return render(request, 'login.html', context)

    def post(self, request):
        """
        Hace login de un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = LoginForm(request.POST)
        context = dict()
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                # usuario autenticado
                request.session["default-language"] = "es"
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)
            else:
                # usuario no autenticado
                context["error"] = "Wrong username or password"
        context["form"] = form
        return render(request, 'login.html', context)

class RegisterView(View):

    def get(self, request):
        """
        Presenta el formulario de login a un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        context = {
            'form': UserCreationForm()
        }

        return render(request, 'register.html', context)

    def post(self, request):
        """
        Hace login de un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = UserCreationForm(request.POST)
        context = dict()
        if form.is_valid():
            user = form.save()

        return redirect('login')

def logout(request):
    """
    asd
    :param request:
    :return:
    """
    django_logout(request)
    return redirect('home')