'''
Crear un proyecto que permita gestionar (administrar) peliculas, colocar
un menu de opciones para agregar, eliminar, modificar, y consultar peliculas.
Notas:
1.- Utiliar funciones y mandar llamar desde otro archivo.
2.- Utilizar listas para almacenar los nombres de peliculas.
3.- 
'''
import peliculas
peliculas.borrarPantalla()
volver=True
pelicula=["Cars","Toy Story","Minecraft"]
while volver:
    peliculas.borrarPantalla()
    op=int(input("Ingrese la opcion que desea: \n1)Agregar pelicula\n2)Eliminar pelicula\n3)Modificar una pelicula\n4)Consultar pelicula\n5)Buscar\n6)Vaciar\n7)Salir\n"))
    peliculas.borrarPantalla()
    match op:
        case 1:
            nueva_pelicula=input("Ingrese la nueva pelicula: ")
            pelicula=peliculas.anadir_Pelicula(pelicula,nueva_pelicula)
            print(pelicula)
            peliculas.espereTecla()
        case 2:
            eliminar_pos=int(input("Ingrese la posicion de la pelicula a eliminar: "))
            pelicula=peliculas.eliminar_pelicula(pelicula,eliminar_pos)
            print(pelicula)
            peliculas.espereTecla()
        case 3:
            indice=int(input("Ingrese la posicion de la pelicula a cambiar: "))
            nueva_pelicula=input("Ingrese la nueva pelicula para esa posicion: ")
            pelicula=peliculas.modificar_pelicula(pelicula,indice,nueva_pelicula)
            print(pelicula)
            peliculas.espereTecla()
        case 4:
            peliculas.consultar_pelicula(pelicula)
            peliculas.espereTecla()
        case 5:
            nombre=input("Ingrese el nombre de la pelicula a buscar: ")
            peliculas.buscar_pelicula(pelicula,nombre)
            peliculas.espereTecla()
        case 6:
            pelicula,mensaje=peliculas.vaciar_lista(pelicula)
            print(mensaje)
            peliculas.espereTecla()
        case 7:
            print("OP 5, Salir")
            volver=False
        case _:
            print("Opcion invalida")
    if op !=7:
        des=input("Desea realizar otro proceso) s/n ").lower()
        if des!= "s":
            volver=False