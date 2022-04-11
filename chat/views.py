from django.views.generic import ListView, CreateView
from .models import Mensaje


class MensajeView(CreateView):
    
    model = Mensaje
    template_name = 'chat/crear_mensaje.html'


class ListaMensajesView(ListView):
    
    model = Mensaje
    template_name = 'chat/listar_mensajes.html'
