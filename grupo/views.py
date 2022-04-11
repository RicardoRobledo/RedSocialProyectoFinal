from django.views.generic import ListView, CreateView
from .models import Grupo


class GruposView(ListView):
    
    model = Grupo
    template_name = 'grupo/grupos.html'
    

class CrearGrupoView(CreateView):
    
    model = Grupo
    template_name = 'grupo/creacion_grupo.html'
    fields = ('nombre_grupo', 'descripcion',) # new
