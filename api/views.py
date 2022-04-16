from rest_framework import viewsets # new
from grupo.models import Grupo
from .permissions import IsAuthorOrReadOnly


# Create your views here.
class GruposViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Grupo.objects.all()
