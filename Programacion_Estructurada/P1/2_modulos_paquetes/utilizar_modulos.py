#Primer forma de utilizar los modulos
import modulos

modulos.borrarPantalla()
print(modulos.saludar("Edson Lomas Corral"))

#Segunda forma de utilizar modulos

from modulos import saludar,borrarPantalla

borrarPantalla()
print(saludar("Luis"))


nombre=input("Ingresa el nombre del contacto: ")
telefono=input("Ingresa el telefono: ")
nom,tel=modulos.solicitarDatos4(nombre,telefono)
print(f"\tNobre completo: {nom}\n\tEl telefono: {tel}")