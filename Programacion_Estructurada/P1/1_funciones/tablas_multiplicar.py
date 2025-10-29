'''
Crear un programa que calcule e imprima cualquier tabla de multiplicar del 2

Requisitos:
1.- SIn estructuras de control
2.- Sin funciones
'''
#print(f"2 x 1 = {2*1}\n2 x 2 = {2*2}\n2 x 3 = {2*3}\n2 x 4 = {2*4}\n2 x 5 = {2*5}\n2 x 6 = {2*6}\n2 x 7 = {2*7}\n2 x 8 = {2*8}\n2 x 9 = {2*9}\n2 x 10 = {2*10}")

#Version 1
num=int(input("Dame el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num} x 1 = {multi}")
multi=num*2
print(f"{num} x 2 = {multi}")
multi=num*3
print(f"{num} x 3 = {multi}")
multi=num*4
print(f"{num} x 4 = {multi}")
multi=num*5
print(f"{num} x 5 = {multi}")
multi=num*6
print(f"{num} x 6 = {multi}")
multi=num*7
print(f"{num} x 7 = {multi}")
multi=num*8
print(f"{num} x 8 = {multi}")
multi=num*9
print(f"{num} x 9 = {multi}")
multi=num*10
print(f"{num} x 10 = {multi}")

#Version 2
num=int(input("Dame el numero de la tabla de multiplicar: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

num=int(input("Dame el numero de la tabla de multiplicar: "))
i=1
while i<=10:
    print(f"{num} x {i} = {num*i}")
    i+=1

#version 3
def tablaMultiplicar(num,limite):
    tabla=""
    for i in range(1,limite+1):
        tabla+=f"{num} x {i} = {num*i}\n"
    return tabla

numero=int(input("Ingrese el numero de la tabla de multiplicar: "))
limite=int(input("Ingrese el limite de la tabla de multiplicar: "))
tabla1=tablaMultiplicar(numero,limite)
print(f"{tabla1}")

