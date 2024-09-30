from rest_framework import serializers
from .models import Articulo, Proveedor, Grupo, Subgrupo, Marca

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'

class SubgrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgrupo
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    proveedores = ProveedorSerializer(many=True, read_only=True)
    grupo = GrupoSerializer(read_only=True)
    subgrupo = SubgrupoSerializer(read_only=True)
    marca = MarcaSerializer(read_only=True)

    class Meta:
        model = Articulo
        fields = '__all__'
