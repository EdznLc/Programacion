from conexionBD import *


class Autos: 
    def __init__ (self, marca, color, modelo, velocidad, caballaje, plazas):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._caballaje = caballaje
        self._plazas = plazas

    def insertar(self):
        try:
            cursor.execute("Insert into coches values(Null, %s, %s, %s, %s, %s, %s)",(self._marca, self._color, self._modelo, self._velocidad, self._caballaje, self._plazas))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from coches")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, id):
        try:
            cursor.execute("Update coches set marca = %s, color= %s, modelo = %s, velocidad = %s, caballaje = %s, plazas = %s where id_coche =%s",(marca, color, modelo, velocidad, caballaje, plazas, id))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from coches where id_coche =%s",(id,))
            conexion.commit()
            return True
        except:
            return False

class Camionetas:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            cursor.execute("insert into camionetas values(NULL, %s, %s, %s, %s, %s, %s, %s, %s)",(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from camionetas")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id):
        try:
            cursor.execute("Update camionetas set marca = %s, color= %s, modelo = %s, velocidad = %s, caballaje = %s, plazas = %s, traccion = %s, cerrada = %s where id_camioneta =%s",(marca, color, modelo, velocidad, caballaje, plazas, traccion,cerrada, id))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from camionetas where id_camioneta =%s",(id,))
            conexion.commit()
            return True
        except:
            return False



class Camion:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad):
        try:
            cursor.execute("insert into camiones values(NULL, %s, %s, %s, %s, %s, %s, %s, %s)",(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from camiones")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad, id):
        try:
            cursor.execute("Update camiones set marca = %s, color= %s, modelo = %s, velocidad = %s, caballaje = %s, plazas = %s, eje = %s, capacidadCarga = %s where id_camiones =%s",(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad, id))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from camiones where id_camiones =%s",(id,))
            conexion.commit()
            return True
        except:
            return False



class Camiones: 
    pass