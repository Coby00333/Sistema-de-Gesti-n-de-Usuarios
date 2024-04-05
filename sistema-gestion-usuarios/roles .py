import hashlib

# Parte 1: Define una clase "Usuario" con atributos y métodos para obtener/establecer esos atributos
class Usuario:
    def __init__(self, nombre, apellido, correo, contraseña):
        # Constructor que inicializa los atributos del usuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = self._encriptar_contraseña(contraseña)

    def _encriptar_contraseña(self, contraseña):
        # Método privado para encriptar la contraseña utilizando hash SHA-256
        return hashlib.sha256(contraseña.encode()).hexdigest()

    # Métodos para obtener los atributos del usuario
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_apellido(self):
        return self.apellido
    
    def obtener_correo(self):
        return self.correo
    
    # Parte 3: Implementa autenticación con encriptación y comparación de contraseñas seguras
    def verificar_contraseña(self, contraseña):
        if self.contraseña == self._encriptar_contraseña(contraseña):
            print("Contraseña verificada: Acceso concedido.")
            return True
        else:
            print("Contraseña incorrecta: Acceso denegado.")
            return False

# Parte 2: Diseña una estructura de clases para roles y permisos
class Rol:
    def __init__(self, nombre):
        self.nombre = nombre
        self.permisos = []

    def agregar_permiso(self, permiso):
        # Método para agregar permisos al rol
        self.permisos.append(permiso)
        print(f"Permiso '{permiso}' agregado al rol '{self.nombre}'.")

    def tiene_permiso(self, permiso):
        # Método para verificar si un rol tiene cierto permiso
        if permiso in self.permisos:
            print(f"El rol '{self.nombre}' tiene el permiso '{permiso}'.")
            return True
        else:
            print(f"El rol '{self.nombre}' no tiene el permiso '{permiso}'.")
            return False

# Parte 4: Utiliza herencia para gestionar distintos tipos de usuarios
class Administrador(Usuario):
    def __init__(self, nombre, apellido, correo, contraseña):
        super().__init__(nombre, apellido, correo, contraseña)
        # Crea un rol de Administrador y asigna permisos específicos
        self.rol = Rol("Administrador")
        self.rol.agregar_permiso("crear_usuario")
        self.rol.agregar_permiso("eliminar_usuario")
        print("Se ha creado un nuevo administrador.")

class UsuarioNormal(Usuario):
    def __init__(self, nombre, apellido, correo, contraseña):
        super().__init__(nombre, apellido, correo, contraseña)
        # Crea un rol de Usuario Normal, sin permisos específicos
        print("Se ha creado un nuevo usuario normal.")

#**********************************************************************************************
# Ejemplo de uso
admin = Administrador("Admin", "Admin", "admin@example.com", "admin123")
user = UsuarioNormal("User", "Normal", "user@example.com", "user123")

# Verificación de contraseña
admin.verificar_contraseña("admin123")  # Output: True (contraseña correcta)
user.verificar_contraseña("wrongpass")  # Output: False (contraseña incorrecta)

# Verificación de permisos
admin.rol.tiene_permiso("crear_usuario")  # Output: True (rol tiene el permiso)
user.rol.tiene_permiso("crear_usuario")   # Output: False (rol no tiene el permiso)
