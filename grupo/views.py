from django.views.generic import ListView
from .models import Grupo


class GruposView(ListView):
    
    model = Grupo
    template_name = 'grupo/grupos.html'
