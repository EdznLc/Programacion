from conexionBD import *
import hashlib
import datetime

class Usuario:
    @staticmethod
    def registrar(nombre, apellidos, email, contrasena):
        try:
            fecha=datetime.datetime.now()
            db = Conexion()
            db.cursor.execute(
                "INSERT INTO usuarios VALUES (NULL, %s, %s, %s, %s, %s)",
                (nombre, apellidos, email, contrasena, fecha)
            )
            db.conexion.commit()
            db.cerrar()
            return True
        except:
            return False

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
            db = Conexion()
            db.cursor.execute(
                "SELECT * FROM usuarios WHERE email=%s AND password=%s",
                (email, contrasena)
            )
            usuario = db.cursor.fetchone()
            db.cerrar()
            return usuario
        except:
            return None
