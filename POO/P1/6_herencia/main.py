from coches import *

#Crear un objetos o instanciar la clase

#Solicitar los datos que seran los atributos del objeto.

"""num_coches = int(input("Cuantos coches tienes?"))
for i in range(0,num_coches):
    print(f"\n\t...Datos del Automovil #{i+1}...")
    marca = input("Ingresa la marca: ").upper()
    color = input("Ingresa el color: ").upper()
    modelo = input("Ingresa el modelo: ").upper()
    velocidad = int(input("Ingresa la velocidad: ").upper())
    potencia = int(input("Ingresa la potencia: ").upper())
    plazas = int(input("Ingresa el # plazas: ").upper())

    coche1 = Coches(marca, color, modelo, velocidad, potencia, plazas)
    print(f"\nDatos del Vehiculo: \n Marca:{coche1.marcam} \n color: {coche1.colorm} \n Modelo: {coche1.modelom} \n velocidad: {coche1.velocidadm} \n caballaje: {coche1.caballajem} \n plazas: {coche1.plazasm}")
"""

coche = Coches("VW", "Blanco", "2020", 220, 180, 4)
print(coche.colorm, coche.acelerar())

camion = Camiones("VW", "Blanco Titanio", "2020", 220, 180, 4, 2, 2500)
print(camion.colorm, camion.acelerar())

camioneta = Camionetas("VW", "Azul", "2020", 220, 180, 4, "Delantera", True)
print(camioneta.colorm, camioneta.acelerar())