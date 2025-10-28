import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "bd_estudiante"
    )
    cursor = conexion.cursor(buffered=True)
except:
    print("Error al conectar con la base de datos")