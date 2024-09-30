from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email.')
        user = self.model(email=self.normalize_email(email), nombre=nombre)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, password):
        user = self.create_user(email, nombre, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Añadimos related_name para evitar conflictos con el modelo auth.User
    groups = models.ManyToManyField(Group, related_name='usuarios_usuario_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_usuario_set', blank=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.email
