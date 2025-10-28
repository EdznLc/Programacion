import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    #Crear los metodos setter y getter, estos metodos son importantes y necesarios en todas las clases para que el programador
    #Interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada
    #para solicitar un valor (get) y/o para ingresar o cambiear un valor (set) a un atributo en particular de la clase a traves de
    #un objeto.
    #En teoria se deberia de crea un metodo Getter y Setter por cada atributo que contenga la clase.
    #Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return.
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion. 

    #1er Forma
    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca

    #2da Forma
    @property
    def marca2(self):
        return self.marca
    
    @marca2.setter
    def marca2(self, marca2):
        self.marca = marca2

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getVelocidad(self):
        return self.velocidad
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def getCaballaje(self):
        return self.caballaje
    
    def setCaballaje(self, caballaje):
        self.caballaje = caballaje

    def getPlazas(self):
        return self.plazas
    
    def setPlazas(self, plazas):
        self.plazas = plazas
    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        pass

    def frenar(self):
        pass  

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1 = Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2 = Coches("Nissan", "Azul", "2020", 180, 150, 6)
coche3 = Coches("Honda", "", "", 0, 0, 0)
coche1.num_serie = "2525052006"
coche4 = Coches("", "", "", 0, 0, 0)


print(f"\nDatos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n Num. Serie: {coche1.num_serie}")
print(f"\nDatos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

coche3.marca2 = "Honda"
print(coche3.marca2)

