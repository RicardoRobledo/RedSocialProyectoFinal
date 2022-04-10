from django.urls import path
from .views import RegistroPageView, InicioSesion

urlpatterns = [
    path('registro/', RegistroPageView.as_view(), name="registro"),
]