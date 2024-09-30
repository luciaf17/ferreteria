# Sistema de Gestión de Ferretería - Módulo de Usuarios

Este es el sistema de gestión de usuarios para la plataforma de gestión de ferreterías. 

## Requisitos

- Python 3.9+
- Django 3.2+
- MySQL (o SQLite para desarrollo)

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio```

2. Crear un entorno virtual e instalar las dependencias:
   ```python -m venv env
    ```. env\Scripts\activate.ps1

3. Instalar las dependencias:
    ```pip install -r requirements.txt```

4. Crear un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:
    ```SECRET_KEY=tu_clave_secreta
    DEBUG=True
    DATABASE_NAME=ferreteria_cliente_db
    DATABASE_USER=root
    DATABASE_PASSWORD=tu_contraseña
    DATABASE_HOST=localhost
    DATABASE_PORT=3306

5. Aplicar las migraciones:
    ```python manage.py migrate

6. Crear un superusuario en el Admin:
    ```python manage.py createsuperuser

7.Iniciar el servidor de desarrollo:
    ```python manage.py runserver

## Ejecutar las pruebas

```python manage.py test usuarios


## Características

-Autenticación de usuarios
-Gestión de usuarios a través de la API REST
-Panel de administración para gestionar usuarios

