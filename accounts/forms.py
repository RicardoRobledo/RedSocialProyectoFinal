from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado


class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        
        model = UsuarioPersonalizado
        fields = ('nombre', 'ap_paterno', 'ap_materno', 'username', 'email')