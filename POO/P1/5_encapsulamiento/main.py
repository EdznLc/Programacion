from coches import *

#Crear un objetos o instanciar la clase

#Solicitar los datos que seran los atributos del objeto.

num_coches = int(input("Cuantos coches tienes?"))
for i in range(0,num_coches):
    print(f"\n\t...Datos del Automovil #{i+1}...")
    marca = input("Ingresa la marca: ").upper()
    color = input("Ingresa el color: ").upper()
    modelo = input("Ingresa el modelo: ").upper()
    velocidad = int(input("Ingresa la velocidad: ").upper())
    potencia = int(input("Ingresa la potencia: ").upper())
    plazas = int(input("Ingresa el # plazas: ").upper())

    coche1 = Coches(marca, color, modelo, velocidad, potencia, plazas)
    print(f"\nDatos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")

"""coche1 = Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2 = Coches("Nissan", "Azul", "2020", 180, 150, 6)
coche3 = Coches("Honda", "", "", 0, 0, 0)
coche1.num_serie = "2525052006"
coche4 = Coches("", "", "", 0, 0, 0)


print(f"\nDatos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n Num. Serie: {coche1.num_serie}")
print(f"\nDatos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

coche3.marca2 = "Honda"
print(coche3.marca2)"""