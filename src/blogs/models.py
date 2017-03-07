from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):

    
    GENERAL = "GEN"
    TECNOLOGIA = "TEC"
    POLITICA = "POL"
    TEMATICAS = (
        (GENERAL, "General"),
        (TECNOLOGIA, "Tecnologia"),
        (POLITICA,"Politica")
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    tematica = models.CharField(max_length=3, default=GENERAL, choices=TEMATICAS)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name="owned_blogs")

    def __str__(self):
        return self.name

class Categoria(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):

    PUBLICADO = "PUB"
    NOPUBLICADO = "NOP"
    ESTADOS = (
        (PUBLICADO, "Publicado"),
        (NOPUBLICADO, "No publicado")
    )

    titulo = models.CharField(max_length=100)
    introduccion = models.CharField(max_length=140)
    cuerpo = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=3, default=NOPUBLICADO, choices=ESTADOS)
    modified_at = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=100,blank=True, null=True)
    owner = models.ForeignKey(Blog, related_name="owned_posts")
    categoria = models.ForeignKey(Categoria, related_name="owned_posts_category")
    # categorías en las que se publican (un post puede publicarse en una o varias categorías).
    # Las categorías deben poder ser gestionadas desde el administrador.

    def __str__(self):
        return self.titulo