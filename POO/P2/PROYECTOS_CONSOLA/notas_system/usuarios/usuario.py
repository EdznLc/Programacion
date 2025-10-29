import hashlib
import datetime

class Usuarios:
    def __init__(self, nombre, apellidos, email, contrasena):
        self._nombre = nombre
        self._apellidos = apellidos
        self._email = email
        self._contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
        self._fecha = datetime.datetime.now()
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_apellidos(self):
        return self._apellidos
    
    def set_apellidos(self, apellidos):
        self._apellidos = apellidos
    
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
    
    def get_contrasena(self):
        return self._contrasena
    
    def set_contrasena(self, contrasena):
        self._contrasena = contrasena