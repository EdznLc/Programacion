'''
la pelicua es: y estaba en la casilla:

se borro x pelicula con este titulo
Crear un proyecto que permita gestionar (administrar) peliculas, colocar
un menu de opciones para agregar, eliminar, modificar, y consultar peliculas.
Notas:
1.- Utiliar funciones y mandar llamar desde otro archivo.
2.- Utilizar listas para almacenar los nombres de peliculas.
3.- 
'''
import peliculasdago

opcion=True
while opcion:
    peliculasdago.borrarPantalla()
    print("\n\t\t..::: CINEPOLIS CLON :::... \n\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar  \n\t\t 2.- Eliminar \n\t\t 3.- Actualizar \n\t\t 4.- Consultar \n\t\t 5.- Buscar \n\t\t 6.- Vaciar \n\t\t 7.- SALIR ")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculasdago.agregarPeliculas()
            peliculasdago.esperarTecla()
        case "2":
            peliculasdago.eliminarPeliculas()
            peliculasdago.esperarTecla() 
        case "3":
            peliculasdago.modificarPeliculas()
            peliculasdago.esperarTecla()    
        case "4":
            peliculasdago.consultarPeliculas()
            peliculasdago.esperarTecla()  
        case "5": 
            peliculasdago.buscarPeliculas()
            peliculasdago.esperarTecla()
        case "6": 
            peliculasdago.vaciarPeliculas()
            peliculasdago.esperarTecla()
        case "7":
            opcion=False    
            peliculasdago.borrarPantalla()
            print("\n\t\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\t\tOpción invalida vuelva a intentarlo ... por favor")