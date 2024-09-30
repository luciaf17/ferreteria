from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'nombre', 'is_active', 'is_staff', 'is_superuser']
