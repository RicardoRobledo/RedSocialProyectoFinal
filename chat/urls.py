from django.urls import path
from .views import ListaMensajesView, MensajeView


urlpatterns = [
    path('conversaciones/<int:pk>/', ListaMensajesView.as_view(), name='chat'),
    path('crear_mensaje/<int:pk>/', MensajeView.as_view(), name='crear_mensaje'),
]
