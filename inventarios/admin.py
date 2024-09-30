from django.contrib import admin
from .models import Articulo, Proveedor, Grupo, Subgrupo, Marca

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo_barra', 'grupo', 'subgrupo', 'marca', 'precio', 'stock']
    search_fields = ['nombre', 'codigo_barra']
    list_filter = ['grupo', 'subgrupo', 'marca']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'contacto', 'telefono', 'email']
    search_fields = ['nombre', 'email']

admin.site.register(Grupo)
admin.site.register(Subgrupo)
admin.site.register(Marca)
