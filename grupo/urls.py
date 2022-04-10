from django.urls import path
from .views import GruposView

urlpatterns = [
    path('grupos/', GruposView.as_view(), name="lista_grupos")
]