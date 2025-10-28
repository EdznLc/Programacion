import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bd_notas'
        )
        self.cursor = self.conexion.cursor(buffered=True)

    def cerrar(self):
        self.cursor.close()
        self.conexion.close()
