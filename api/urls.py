from django.urls import path
from .views import GruposViewSet


urlpatterns = [
    path('', GruposViewSet.as_view(), name='home'),
]
