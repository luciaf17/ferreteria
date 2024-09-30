from rest_framework import viewsets
from .models import Articulo, Proveedor, Grupo, Subgrupo, Marca
from .serializers import ArticuloSerializer, ProveedorSerializer, GrupoSerializer, SubgrupoSerializer, MarcaSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class SubgrupoViewSet(viewsets.ModelViewSet):
    queryset = Subgrupo.objects.all()
    serializer_class = SubgrupoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
