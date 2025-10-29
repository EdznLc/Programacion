'''
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas 
pequenio que cumple una funcion especifica. La funcion de puede reutilizar con el simple hecho sde invocarla
es decir mendarla a llamar.

Sintaxis:

def nombredeMifuncion(parametros):
    bloque o conjunto de instrucciones

def nombredeMifuncion(parametros):
    bloque o conjunto de instrucciones

Las funciones pueden ser de 4 tipos

Funciones de tipo "Procedimiento".
1.- Funcion que no recibe parametros y no regresa valor.
3.- Funcion que recibe parametros y no regresa valor.

Funciones de tipo "Funcion"
2.- Funcion que no recibe parametros y regresa valor
4.- Funcion que recibe parametros y regresa valor


'''

#1.-Funcion que no recibe parametro y no regresa valor
def solicitarDatos1():
    nombre=input("Ingresa el nombre: ")
    telefono=input("Ingresa el numero de telefono: ")
    print(f"Soy funcion 1-.-El nombre es: {nombre} y su telefono es: {telefono}")


#3.-Funcion que recibe parametros y no regresa valor.
def solicitarDatos3(nombre,telefono):
    print(f"Soy funcion 3-.-El nombre es: {nombre} y su telefono es: {telefono}")

#2.-Funcion que no recibe parametros y regresa valor
def solicitarDatos2():
    nombre=input("Ingresa el nombre: ")
    telefono=input("Ingresa el numero de telefono: ")
    return nombre,telefono

#4.-Funcion que recibe parametros y regresa valor
def solicitarDatos4(nombre,telefono):
    return nombre,telefono

#Llamar las funciones
solicitarDatos1()

nombre=input("Ingresa el nombre: ")
telefono=input("Ingresa el numero de telefono: ")
solicitarDatos3(nombre,telefono)

nombre,telefono=solicitarDatos2()
print(f"Nombre: {nombre}?]\nTelefono: {telefono}")


nombre=input("Ingresa el nombre: ")
telefono=input("Ingresa el numero de telefono: ")
nombre,telefono=solicitarDatos4(nombre,telefono)
print(f"Nombre: {nombre}\nTelefono: {telefono}")