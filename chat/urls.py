from django.urls import path
from .views import ListaMensajesView, MensajeView


urlpatterns = [
    path('conversaciones/', ListaMensajesView.as_view(), name='chat')
]
