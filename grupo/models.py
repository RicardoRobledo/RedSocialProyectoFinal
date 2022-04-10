from turtle import ondrag
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model


class Grupo(models.Model):
    
    nombre_grupo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, default="Sin descripcion")
    fecha = models.DateTimeField(auto_now_add=True)
    propietario = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.nombre_grupo