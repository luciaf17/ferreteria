from django.db import models
from django.conf import settings  # Para obtener el modelo de usuario
from simple_history.models import HistoricalRecords  # Para el historial de cambios

# Modelo para agrupar los artículos
class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='grupos_creados', on_delete=models.SET_NULL, null=True, blank=True
    )
    modificado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='grupos_modificados', on_delete=models.SET_NULL, null=True, blank=True
    )
    history = HistoricalRecords()  # Historial de cambios

    def __str__(self):
        return self.nombre

# Modelo para los subgrupos de los artículos
class Subgrupo(models.Model):
    nombre = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, related_name='subgrupos', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='subgrupos_creados', on_delete=models.SET_NULL, null=True, blank=True
    )
    modificado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='subgrupos_modificados', on_delete=models.SET_NULL, null=True, blank=True
    )
    history = HistoricalRecords()  # Historial de cambios

    def __str__(self):
        return f'{self.grupo.nombre} - {self.nombre}'

# Modelo de proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='proveedores_creados', on_delete=models.SET_NULL, null=True, blank=True
    )
    modificado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='proveedores_modificados', on_delete=models.SET_NULL, null=True, blank=True
    )
    history = HistoricalRecords()  # Historial de cambios

    def __str__(self):
        return self.nombre

# Modelo para las marcas de los artículos
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='marcas_creadas', on_delete=models.SET_NULL, null=True, blank=True
    )
    modificado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='marcas_modificadas', on_delete=models.SET_NULL, null=True, blank=True
    )
    history = HistoricalRecords()  # Historial de cambios

    def __str__(self):
        return self.nombre

# Modelo para los artículos
class Articulo(models.Model):
    codigo = models.AutoField(primary_key=True)  # Código autoincremental
    codigo_barra = models.CharField(max_length=13, unique=True)
    nombre = models.CharField(max_length=255)
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)
    subgrupo = models.ForeignKey(Subgrupo, on_delete=models.SET_NULL, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    proveedores = models.ManyToManyField(Proveedor)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='articulos_creados', on_delete=models.SET_NULL, null=True, blank=True
    )
    modificado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='articulos_modificados', on_delete=models.SET_NULL, null=True, blank=True
    )
    history = HistoricalRecords()  # Historial de cambios

    def __str__(self):
        return f'{self.nombre} ({self.codigo_barra})'
