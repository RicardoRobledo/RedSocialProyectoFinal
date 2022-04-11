from django.views.generic import ListView, CreateView
from .models import Grupo


class GruposView(ListView):
    
    model = Grupo
    template_name = 'grupo/grupos.html'
    

class CrearGrupoView(CreateView):
    
    model = Grupo
    template_name = 'grupo/creacion_grupo.html'
    fields = ('nombre_grupo', 'descripcion',)
    
    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)