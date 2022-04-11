from django.urls import path
from .views import GruposView, CrearGrupoView

urlpatterns = [
    path('grupos/', GruposView.as_view(), name="lista_grupos"),
    path('crear_grupo/', CrearGrupoView.as_view(), name="crear_grupo")
]