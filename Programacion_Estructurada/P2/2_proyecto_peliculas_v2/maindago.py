'''
la pelicua es: y estaba en la casilla:

se borro x pelicula con este titulo
Crear un proyecto que permita gestionar (administrar) peliculas, colocar
un menu de opciones para agregar, eliminar, modificar, y consultar peliculas.
Notas:
1.- Utiliar funciones y mandar llamar desde otro archivo.
2.- Utilizar dict para almacenar los diguientes atributos: (nombre, categoria, clasificacion, genero, idioma) de las peliculas
3.- 
'''
import peliculasdago

opcion=True
while opcion:
    peliculasdago.borrarPantalla()
    print("\n\t\t..::: CINEPOLIS CLON :::... \n\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Agregar caracteristicas \n\t\t 5.- Modificar Caracteristicas \n\t\t 6.- Borrar Caracteristicas \n\t\t 7.- SALIR ")
    opcion=input("\n\t\t ✅Elige una opción: ").upper()

    match opcion:
        case "1":
            
            peliculasdago.crearPeliculas()
            peliculasdago.esperarTecla()
        case "2":
            peliculasdago.borrarPeliculas()
            peliculasdago.esperarTecla() 
        case "3":
            peliculasdago.mostrarPeliculas()
            peliculasdago.esperarTecla()    
        case "4":
            peliculasdago.agregarCaracteristicasPeliculas()
            peliculasdago.esperarTecla()  
        case "5": 
            peliculasdago.modificarCaracteristicaPeliculas()
            peliculasdago.esperarTecla()
        case "6": 
            peliculasdago.borrarCaracteristicaPeliculas()
            peliculasdago.esperarTecla()
        case "7":
            opcion=False    
            peliculasdago.borrarPantalla()
            print("\n\t\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\t\tOpción invalida vuelva a intentarlo ... por favor")