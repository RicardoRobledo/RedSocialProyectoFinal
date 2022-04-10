from django.contrib.auth.models import AbstractUser
from django.db import models


class UsuarioPersonalizado(AbstractUser):

    name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
