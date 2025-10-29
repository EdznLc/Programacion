'''
Un modulo es simplemente un archivo con etension .py que contiene
codigo de python (funciones,clases,variables,etc.).

Un paquete es una carpeta que contiene varios modulos (archivos .py)
y un archivo especial llamado __init__.py que le indica a pyhton
que esa carpeta debe tratarse como un paquete.
'''
import os
def borrarPantalla():
    os.system("cls")

def espereTecla():
    input("-.-Oprima una tecla para continuar-.-")

def solicitarDatos1():
    nombre=input("Ingresa el nombre: ")
    telefono=input("Ingresa el numero de telefono: ")
    print(f"Soy funcion 1-.-El nombre es: {nombre} y su telefono es: {telefono}")

def solicitarDatos3(nombre,telefono):
    print(f"Soy funcion 3-.-El nombre es: {nombre} y su telefono es: {telefono}")

def solicitarDatos2():
    nombre=input("Ingresa el nombre: ")
    telefono=input("Ingresa el numero de telefono: ")
    return nombre,telefono

def solicitarDatos4(nombre,telefono):
    return nombre,telefono

def saludar(nombre):
    return f"Hola bienvenido {nombre}"