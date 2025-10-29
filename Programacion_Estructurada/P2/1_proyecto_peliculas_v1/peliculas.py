import os
def borrarPantalla():
    os.system("cls")

def espereTecla():
    input("-.-Oprima una tecla para continuar-.- ")

def anadir_Pelicula(lista,nuevo_valor):
    lista.append(nuevo_valor)
    return lista

def eliminar_pelicula(lista,pos):
    lista.pop(pos)
    return lista

def modificar_pelicula(lista,indice,nueva_pelicula):
    lista[indice]=nueva_pelicula
    return lista

def consultar_pelicula(lista):
    print(lista)

def buscar_pelicula(lista,nombre):
    igual=nombre in lista
    if igual:
        print(f"Se ha encontrado la pelicula: {nombre} en la taquilla: {lista.index(nombre)}")
    else:
        print("No se encuentra la pelicula")

def vaciar_lista(lista):
    op=input("Esta seguro de querer vaciar la lista? s/n ").lower()
    if op=="s":
        lista.clear()
        return lista,"Se ha vaciado la lista"
    elif op=="n":
        return lista,"Se ha cancelado el proceso"
    else:
        return lista,"Ha introducido una opcion incorrecta, se ha cancelado el proceso"