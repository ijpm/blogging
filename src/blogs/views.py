from django.http import HttpResponse
from django.shortcuts import render

def helloworld(request):
    name = request.GET.get("name", "world")
    return HttpResponse("Hello " + name)
