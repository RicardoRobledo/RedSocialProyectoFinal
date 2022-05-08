from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


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
    
    def get_absolute_url(self):
        return reverse('lista_grupos')


# Vista
class MiVista(models.Model):
    
    username = models.CharField(max_length=50)
    cantidad_grupos = models.IntegerField(primary_key=True)
    
    class Meta:
        managed = False
        db_table = "mi_vista"
