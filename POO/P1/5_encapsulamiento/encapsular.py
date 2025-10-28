import os
os.system("cls")
class Clase:
    atributo_publico = "Soy un atributo publico"
    _atributo_protegido = "Soy un atributo protegido"
    __atributo_privado = "Soy un atributo privado"

    def __init__(self, color, size):
        self.__color = color
        self.__size = size

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        self.__color = size

    def __getAtributoPrivado(self):
        return self.__atributo_privado
    
    def getAtributoPrivado2(self):
        return self.__getAtributoPrivado
    
    def setAtributoPrivado(self, atributo_privado):
        self.__atributo_privado = atributo_privado


#Usar los atributos y metodos de acuerdo a su encapsulamiento
objeto = Clase("Rojo", "Grande")
print(f"Mi objeto tiene los siguientes atributos: {objeto.color} y {objeto.size}")

print(f"Soy el contenido del atributo publico: {objeto.atributo_publico}")
print(f"Soy el contenido del atributo protegido: {objeto._atributo_protegido}")
print(f"Soy el contenido del atributo privado: {objeto._getAtributoPrivado2()}")
objeto.setAtributoPrivado("Se ha cambiado el valor del atributo privado")
print(f"Soy el contenido del atributo privado: {objeto._getAtributoPrivado2()}")
