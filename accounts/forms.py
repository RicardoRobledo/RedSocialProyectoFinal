from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioPersonalizado


class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        
        model = UsuarioPersonalizado
        fields = ('name', 'middle_name', 'last_name', 'username', 'email')


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        
        model = UsuarioPersonalizado
        fields = ('name', 'middle_name', 'last_name', 'username', 'email')