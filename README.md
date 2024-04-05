**README.md**

# Sistema de Gestión de Usuarios

Este repositorio contiene un sistema de gestión de usuarios desarrollado en Python. El sistema permite crear diferentes tipos de usuarios, como administradores y usuarios normales, y asignar roles y permisos correspondientes. Además, proporciona funcionalidades para la autenticación segura de usuarios mediante la encriptación de contraseñas.

## Características

- Creación de usuarios con atributos como nombre, apellido, correo electrónico y contraseña.
- Asignación de roles y permisos a los usuarios, incluyendo roles de administrador y usuarios normales.
- Autenticación segura de usuarios mediante encriptación de contraseñas.
- Flexibilidad en la gestión de usuarios mediante el uso de herencia y interfaces.

## Estructura del repositorio

- `usuario.py`: Contiene la implementación de la clase `Usuario` que representa un usuario en el sistema.
- `rol.py`: Contiene la implementación de la clase `Rol` que define los roles y permisos de los usuarios.
- `administrador.py`: Contiene la implementación de la clase `Administrador` que representa un administrador en el sistema.
- `usuario_normal.py`: Contiene la implementación de la clase `UsuarioNormal` que representa un usuario normal en el sistema.
- `main.py`: Archivo principal que muestra ejemplos de uso del sistema.

## Ejemplos de uso

El archivo `main.py` contiene ejemplos de uso del sistema de gestión de usuarios. Incluye la creación de usuarios, la verificación de contraseñas y permisos, entre otras funcionalidades.

## Requisitos

- Python 3.x

## Instalación

1. Clona el repositorio a tu máquina local:

```
git clone https://github.com/tu_usuario/sistema-gestion-usuarios.git
```

2. Navega al directorio del repositorio:

```
cd sistema-gestion-usuarios
```

3. Ejecuta el archivo `roles.py` para ver ejemplos de uso:

```
python roles.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o deseas mejorar el sistema, por favor crea un issue o envía un pull request.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).
