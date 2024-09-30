from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, GrupoViewSet, SubgrupoViewSet, ProveedorViewSet, ArticuloViewSet

router = DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'grupos', GrupoViewSet)
router.register(r'subgrupos', SubgrupoViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'articulos', ArticuloViewSet)

urlpatterns = router.urls
