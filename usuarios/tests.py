from django.test import TestCase
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class UsuarioTests(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            email='usuario@example.com',
            nombre='Usuario Test',
            password='testpassword123'
        )

    def test_creacion_usuario(self):
        """Prueba que se puede crear un usuario correctamente."""
        self.assertEqual(self.usuario.email, 'usuario@example.com')
        self.assertEqual(self.usuario.nombre, 'Usuario Test')
        self.assertTrue(self.usuario.check_password('testpassword123'))

    def test_creacion_superusuario(self):
        """Prueba que se puede crear un superusuario correctamente."""
        superusuario = Usuario.objects.create_superuser(
            email='admin@example.com',
            nombre='Admin Test',
            password='adminpassword123'
        )
        self.assertEqual(superusuario.email, 'admin@example.com')
        self.assertTrue(superusuario.is_superuser)
        self.assertTrue(superusuario.is_staff)
