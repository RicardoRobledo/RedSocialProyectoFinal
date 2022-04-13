from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
class Mensaje(models.Model):
    
    grupo = models.ForeignKey(
        'grupo.Grupo',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    mensaje = models.CharField(max_length=200)
    propietario = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.mensaje

    def get_absolute_url(self):
        return reverse('lista_grupos')
