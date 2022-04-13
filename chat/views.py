from django.views.generic import ListView, CreateView
from .models import Mensaje


class MensajeView(CreateView):
    
    model = Mensaje
    template_name = 'chat/crear_mensaje.html'
    fields = ('mensaje',)

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)


class ListaMensajesView(ListView):

    model = Mensaje
    template_name = 'chat/listar_mensajes.html'
    
    # buscar por filtro de clave
    def get_queryset(self):
       return Mensaje.objects.filter(grupo=self.kwargs['pk'])
