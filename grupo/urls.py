from django.urls import path
from .views import GruposView, CrearGrupoView, reporte, grafica, EliminarGrupoView, EditarGrupoView

urlpatterns = [
    path('grupos/', GruposView.as_view(), name="lista_grupos"),
    path('grafica/', grafica, name="grafica"),
    path('crear_grupo/', CrearGrupoView.as_view(), name="crear_grupo"),
    path('generar_reporte/', reporte, name="generar_reporte"),
    path('eliminar_grupo/<int:pk>/',EliminarGrupoView.as_view(), name='eliminar_grupo'),
    path('editar_grupo/<int:pk>/', EditarGrupoView.as_view(), name='editar_grupo'),
]