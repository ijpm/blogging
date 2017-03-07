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