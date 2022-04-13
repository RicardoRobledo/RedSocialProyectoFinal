from django.views.generic import ListView, CreateView
from .models import Grupo
from django.db import transaction


class GruposView(ListView):
    
    model = Grupo
    template_name = 'grupo/grupos.html'
    

class CrearGrupoView(CreateView):
    
    model = Grupo
    template_name = 'grupo/creacion_grupo.html'
    fields = ('nombre_grupo', 'descripcion',)
    
    @transaction.atomic
    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)