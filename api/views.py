from rest_framework import viewsets # new
from grupo.models import Grupo
from .permissions import IsAuthorOrReadOnly
from .serializers import GrupoSerializer, UserSerializer
from django.contrib.auth import get_user_model # new


# Create your views here.
class GruposViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
