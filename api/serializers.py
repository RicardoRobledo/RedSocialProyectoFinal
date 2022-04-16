from rest_framework import serializers
from grupo.models import Grupo
from django.contrib.auth import get_user_model # new


class GrupoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('nombre_grupo', 'descripcion', 'fecha', 'propietario',)
        model = Grupo


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)