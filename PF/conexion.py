import mysql.connector
from mysql.connector import Error
try:
    conexion=mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "",
        database = "bd_ventaropa"
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("Ocurrio algo inesperado con la base de datos ...")