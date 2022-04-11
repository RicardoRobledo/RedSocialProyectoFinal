from django.db import models
from django.contrib.auth import get_user_model
from grupo.models import Grupo


# Create your models here.
class Mensaje(models.Model):
    
    propietario = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.CASCADE,
        related_name='grupos',
    )
    mensaje = models.CharField(max_length=200)
    
