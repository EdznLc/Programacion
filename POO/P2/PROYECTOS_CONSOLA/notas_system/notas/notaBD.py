from conexionBD import *

class Nota:
    @staticmethod
    def crear(id, titulo, descripcion):
        try:
            db = Conexion()
            db.cursor.execute(
                "INSERT INTO notas VALUES (NULL, %s, %s, %s, NOW())",
                (id, titulo, descripcion)
            )
            db.conexion.commit()
            db.cerrar()
            return True
        except:
            return False

    @staticmethod
    def mostrar(usuario_id):
        try:
            db = Conexion()
            db.cursor.execute(
                "SELECT * FROM notas WHERE usuario_id=%s",
                (usuario_id,)
            )
            nota = db.cursor.fetchall()
            db.cerrar()
            return nota
        except:
            return []

    @staticmethod
    def actualizar(titulo, descripcion, id):
        try:
            db = Conexion()
            db.cursor.execute(
                "UPDATE notas SET titulo=%s, descripcion=%s WHERE id=%s",
                (titulo, descripcion, id)
            )
            db.conexion.commit()
            db.cerrar()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id):
        try:
            db = Conexion()
            db.cursor.execute("DELETE FROM notas WHERE id=%s", (id,))
            db.conexion.commit()
            return True
        except:
            return False
