'''
Proyecto 3
Crear un proyecto que permita Gestionar (administrar) calificaciones, colocar un menu de opciones para agregar, mostrar,
calcular promedio calificaciones de un estudiante. 
Notas:
1.- Utiliar funciones y mandar llamar desde otro archivo.
2.- Utilizar list (bidimencional) para almacenar el nombre del alumno, asi como sus 3 calificaciones.
3.- 
'''
import calificaciones

def main():
    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principlal()
        match opcion:
            case "1":
                calificaciones.agregar_calificaciones()
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones()
                calificaciones.esperarTecla() 
            case "3":
                calificaciones.calcular_promedios()
                calificaciones.esperarTecla()    
            case "4":
                calificaciones.buscarAlumno()
                calificaciones.esperarTecla()    
            case "5":
                opcion=False    
                calificaciones.borrarPantalla()
                print("\n\t\t 🥺​ Terminaste la ejecucion del SW 🥺​ ")
            case _: 
                input("\n\t\t 🚫 Opción invalida vuelva a intentarlo ...")

if __name__=="__main__":
    main()