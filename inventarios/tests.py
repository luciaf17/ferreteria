from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Articulo, Proveedor, Grupo, Subgrupo, Marca

# Obtener el modelo de usuario personalizado
Usuario = get_user_model()

class InventariosModelTests(TestCase):
    
    def setUp(self):
        # Crear un usuario para los campos 'creado_por' y 'modificado_por'
        self.usuario = Usuario.objects.create_user(
            email='usuario@test.com',
            nombre='Usuario Test',
            password='test123'
        )
        
        # Crear una marca
        self.marca = Marca.objects.create(nombre="MarcaTest", creado_por=self.usuario, modificado_por=self.usuario)
        
        # Crear un grupo y subgrupo
        self.grupo = Grupo.objects.create(nombre="Herramientas", creado_por=self.usuario, modificado_por=self.usuario)
        self.subgrupo = Subgrupo.objects.create(nombre="Manuales", grupo=self.grupo, creado_por=self.usuario, modificado_por=self.usuario)

        # Crear un proveedor
        self.proveedor = Proveedor.objects.create(
            nombre="ProveedorTest",
            contacto="ContactoTest",
            telefono="123456789",
            email="proveedor@test.com",
            creado_por=self.usuario,
            modificado_por=self.usuario
        )

        # Crear un artículo
        self.articulo = Articulo.objects.create(
            codigo_barra="1234567890123",
            nombre="Martillo",
            grupo=self.grupo,
            subgrupo=self.subgrupo,
            marca=self.marca,
            precio=9.99,
            stock=50,
            descripcion="Martillo de prueba",
            creado_por=self.usuario,
            modificado_por=self.usuario
        )
        self.articulo.proveedores.add(self.proveedor)  # Relación ManyToMany

    def test_creacion_marca(self):
        """Prueba que se pueda crear una marca correctamente y verificar auditoría"""
        self.assertEqual(self.marca.nombre, "MarcaTest")
        self.assertEqual(self.marca.creado_por, self.usuario)
        self.assertEqual(self.marca.modificado_por, self.usuario)
        self.assertTrue(self.marca.fecha_creacion <= timezone.now())

    def test_creacion_grupo(self):
        """Prueba que se pueda crear un grupo y subgrupo correctamente y verificar auditoría"""
        self.assertEqual(self.grupo.nombre, "Herramientas")
        self.assertEqual(self.subgrupo.nombre, "Manuales")
        self.assertEqual(self.subgrupo.grupo, self.grupo)
        self.assertEqual(self.grupo.creado_por, self.usuario)
        self.assertTrue(self.grupo.fecha_creacion <= timezone.now())

    def test_creacion_proveedor(self):
        """Prueba que se pueda crear un proveedor y verificar auditoría"""
        self.assertEqual(self.proveedor.nombre, "ProveedorTest")
        self.assertEqual(self.proveedor.telefono, "123456789")
        self.assertEqual(self.proveedor.email, "proveedor@test.com")
        self.assertEqual(self.proveedor.creado_por, self.usuario)
        self.assertTrue(self.proveedor.fecha_creacion <= timezone.now())

    def test_creacion_articulo(self):
        """Prueba que se pueda crear un artículo y verificar auditoría"""
        self.assertEqual(self.articulo.nombre, "Martillo")
        self.assertEqual(self.articulo.codigo_barra, "1234567890123")
        self.assertEqual(self.articulo.grupo, self.grupo)
        self.assertEqual(self.articulo.subgrupo, self.subgrupo)
        self.assertEqual(self.articulo.marca, self.marca)
        self.assertEqual(self.articulo.precio, 9.99)
        self.assertEqual(self.articulo.stock, 50)
        self.assertEqual(self.articulo.creado_por, self.usuario)
        self.assertTrue(self.articulo.fecha_creacion <= timezone.now())

    def test_articulo_tiene_proveedor(self):
        """Prueba que el artículo tiene al menos un proveedor"""
        self.assertIn(self.proveedor, self.articulo.proveedores.all())

    def test_modificacion_articulo(self):
        """Prueba que se actualice el campo 'modificado_por' al modificar el artículo"""
        nuevo_usuario = Usuario.objects.create_user(
            email='nuevo_usuario@test.com',
            nombre='Nuevo Usuario',
            password='test1234'
        )
        # Modificar el artículo
        self.articulo.nombre = "Martillo Modificado"
        self.articulo.modificado_por = nuevo_usuario
        self.articulo.save()

        # Verificar que el campo 'modificado_por' se actualizó correctamente
        self.assertEqual(self.articulo.nombre, "Martillo Modificado")
        self.assertEqual(self.articulo.modificado_por, nuevo_usuario)
        self.assertTrue(self.articulo.fecha_modificacion >= self.articulo.fecha_creacion)
