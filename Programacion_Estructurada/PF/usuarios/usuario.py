from conexion import *
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre, apellidos, email, contrasena):
    try:
        contrasena=hash_password(contrasena)
        cursor.execute("INSERT INTO usuarios (id, nombre, apellidos, correo, password) VALUES (NULL, %s, %s, %s, %s)",(nombre, apellidos, email, contrasena))
        conexion.commit()
        return True
    except Exception as e:
        print(f"\n⚠️  Error al registrar usuario, correo duplicado  ⚠️")
        return None

def login(email, contrasena):
    try:
        contrasena = hash_password(contrasena)
        cursor.execute("SELECT * FROM usuarios WHERE correo=%s and password=%s", (email, contrasena))
        registro = cursor.fetchone()
        if registro:
            return registro
    except Exception as e:
        print(f"⚠️  Error al iniciar sesión: {e}  ⚠️")
        return None