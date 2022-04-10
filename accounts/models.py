from django.contrib.auth.models import AbstractUser
from django.db import models


class UsuarioPersonalizado(AbstractUser):

    nombre = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
