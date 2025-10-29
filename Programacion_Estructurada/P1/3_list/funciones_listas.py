'''

List(Array)
Son colecciones o conjunto de datos/valores bajo un mismo nombre,
para acceder a los valores se hace con un indice numerico.

Nota: Sus valores son modificables.

La lista es una coleccion ordenada y modificable.
Permite miembros duplicados.


'''
import os
os.system("cls")

paises=["Mexico","Brasil","Espana","Canada"]
numeros=[23,12,100,34]

#Ordenar ascendentemente

print(numeros)
numeros.sort()
print(numeros)

print(paises)
paises.sort()
print(paises)

#Ingresar elementos a una lista
#1er forma
print(paises)
paises.append("Honduras")

#2nda forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar elementos de una lista
#1er forma
paises.pop(1)
print(paises)
#2nda forma
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista
#1er forma
igual="Brasil" in paises
if igual:
    print("Muy bien")
else:
    print("Muy mal")

for i in range(0,len(paises)):
    if paises[i]=="Brasil":
        print("GG")
        break
    else:
        print("ff")


#Cuantas veces aparece un elemento dentro de la lista.
numeros.append(12)
print(f"El numero aparece {numeros.count(12)} vez o veces")

#Identificar el indice de un valor
indice=paises.index("Espana")
paises.pop(indice)
print(paises)

#Recorrer una lista
#1er forma
for i in paises:
    print(i)

#2nda forma
for i in range(0, len(paises)):
    print(f"El valor {i} es: {paises[i]}")

print(paises)
print(numeros)
paises.extend(numeros)
print(paises)