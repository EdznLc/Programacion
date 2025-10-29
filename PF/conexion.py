import mysql.connector
from mysql.connector import Error

class Conexion:
    conexion = None
    cursor = None

    @classmethod
    def establecer_conexion(cls, host="127.0.0.1", user="root", password="", database="bd_ventaropa"):
        try:
            cls.conexion = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            cls.cursor = cls.conexion.cursor(buffered=True)
            return True
        except Error as e:
            print(f"Ocurrio algo inesperado con la base de datos: {e}")
            return False

# Intentamos establecer la conexión al importar
Conexion.establecer_conexion()