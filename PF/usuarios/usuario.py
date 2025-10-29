from conexion import Conexion
import hashlib

class Usuario:
    
    @staticmethod
    def hash_password(contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    @staticmethod
    def registrar(nombre, apellidos, email, contrasena):
        try:
            contrasena_hasheada = Usuario.hash_password(contrasena)
            Conexion.cursor.execute("INSERT INTO usuarios (id, nombre, apellidos, correo, password) VALUES (NULL, %s, %s, %s, %s)",
                                    (nombre, apellidos, email, contrasena_hasheada))
            Conexion.conexion.commit()
            return True
        except Exception as e:
            print(f"\n⚠️  Error al registrar usuario, correo duplicado o error de BD: {e}  ⚠️")
            return None

    @staticmethod
    def login(email, contrasena):
        try:
            contrasena_hasheada = Usuario.hash_password(contrasena)
            Conexion.cursor.execute("SELECT * FROM usuarios WHERE correo=%s and password=%s", (email, contrasena_hasheada))
            registro = Conexion.cursor.fetchone()
            if registro:
                return registro
            return None
        except Exception as e:
            print(f"⚠️  Error al iniciar sesión: {e}  ⚠️")
            return None