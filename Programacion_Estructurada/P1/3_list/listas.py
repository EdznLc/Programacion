import os

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

numeros=[1,2,3,4,5,6,7,8,9,10]
print(numeros)
for i in numeros:
    print(i)
for i in range(0,len(numeros)):
    print(numeros[i])

#crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
os.system("cls")
palabra=["Jose","Luis","Fernan","Diego"]
buscar=input("Ingrese la palabra a buscar: ")

#1er forma
if buscar in palabra:
    print(f"Se encontro {palabra.count("Jose")} vez o veces")
else:
    print("No se encontro la palabra")

#2da forma
encontrado=False
for i in range(0,len(palabra)):
    if palabra[i]==buscar:
        print("Se encontro la palabra")
        encontrado=True

if encontrado==False:
    print("No se encontro la palabra")


input("Oprima una tecla para continuar")


#Ejemplo 3 Anadir elementos a una lista

numeros=[]
os.system("cls")
opc=True
while opc:
    numero=float(input("Ingrese el numero a ingresar en la lista: "))
    numeros.append(numero)
    des=input("Deseas ingresar otro numero? ")
    if des!="si" and des!="s":
        opc=False

print(numeros)



#Ejemplo 4 Crear una lista multidimensional que sea una agenda
os.system("cls")
agenda=[
    ["Carlos","6181234567"],
    ["Alberto","6671234567"],
    ["Martin","6785678923"]
    ]
print(agenda)

for i in agenda:
    print(i)

cadena=""
for r in range(0,3):
    for c in range(0,2):
        #print(agenda[r][c], agenda[r][c+1])
        cadena+=f"{agenda[r][c]},"
    cadena+="\n"

print(f"{cadena}")