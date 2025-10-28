import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._caballaje = caballaje
        self._plazas = plazas

    #Crear los metodos setter y getter, estos metodos son importantes y necesarios en todas las clases para que el programador
    #Interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada
    #para solicitar un valor (get) y/o para ingresar o cambiear un valor (set) a un atributo en particular de la clase a traves de
    #un objeto.
    #En teoria se deberia de crea un metodo Getter y Setter por cada atributo que contenga la clase.
    #Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return.
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion. 

    #2da Forma
    @property
    def marcam(self):
        return self._marca
    
    @marcam.setter
    def marcam(self, marca2):
        self._marca = marca2

    @property
    def colorm(self):
        return self._color
    
    @colorm.setter
    def colorm(self, color):
        self._color = color

    @property
    def modelom(self):
        return self._modelo
    
    @modelom.setter
    def modelom(self, modelo):
        self._modelo = modelo

    @property
    def velocidadm(self):
        return self._velocidad
    
    @velocidadm.setter
    def velocidadm(self, velocidad):
        self._velocidad = velocidad

    @property
    def caballajem(self):
        return self._caballaje
    
    @caballajem.setter
    def caballajem(self, caballaje):
        self._caballaje = caballaje

    @property
    def plazasm(self):
        return self._plazas
    
    @plazasm.setter
    def plazasm(self, plazas):
        self._plazas = plazas
    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        return "Estas acelerando"

    def frenar(self):
        return "Estas frenando" 

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        super().__init__( marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje = eje
        self.__capacidadCarga = capacidadCarga

    def cargar(self, tipo_carga):
        self.tipo_carga = tipo_carga
        return self.tipo_carga
    
    def acelerar(self):
        return "Estas acelerando el camion"
    
    def frenar(self):
        return "Estas frenando el camion"
    
    @property
    def ejem(self):
        return self.__eje
    
    @ejem.setter
    def ejem(self, eje):
        self.__eje = eje

    @property
    def capacidadCargam(self):
        return self.__capacidadCarga
    
    @capacidadCargam.setter
    def capacidadCargam(self, capacidadCarga):
        self.__capacidadCarga = capacidadCarga



class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        super().__init__( marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion = traccion
        self.__cerrada = cerrada
    
    def transportar(self, num_pasjeros):
        self.num_pasajeros = num_pasjeros
        return self.num_pasajeros
    
    def acelerar(self):
        return "Estas acelerando la camioneta"
    
    def frenar(self):
        return "Estas frenando la camioneta"
    
    @property
    def traccionm(self):
        return self.__traccion
    
    @traccionm.setter
    def traccionm(self, traccion):
        self.__traccion = traccion

    @property
    def cerradam(self):
        return self.__cerrada
    
    @cerradam.setter
    def cerradam(self, cerrada):
        self.__cerrada = cerrada

#Fin definir clase



