import funciones
from usuarios import usuario
from notas import nota
import getpass


def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            resultado=usuario.registrar(nombre, apellidos, email, password)
            if resultado:
                print(f"\n\t{nombre} {apellidos}, se registro correctamente, con el email {email}")
            else:
                print(f"\n\t...Por favor intentelo de nuevo, no fue posible registrar al usuario...")
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            registro=usuario.login(email, password)
            if registro:
                menu_notas(registro[0], registro[1], registro[2])
            else:
                print("\n\tEmail y/o contrasena incorrecta, vuelva a intentarlo...")
            funciones.esperarTecla()
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            registro=nota.crear(usuario_id, titulo, descripcion)
            if registro:
                print(f"Se creo la nota {titulo} exitosamente")
            else:
                print("No se pudo crear la nota, vuelve a intentar...")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_nota=nota.mostrar(usuario_id)
            if len(lista_nota)>0:
                print(f"{'-'*70}")
                print(f"{'ID':<10} {'Titulo':<15} {'Descripcion':<25} {'Fecha':<10}")
                print(f"{'-'*70}")
                for registro in lista_nota:
                    print(f"{registro[0]:<10}{registro[2]:<15} {registro[3]:<25} {registro[4]}")
                    print(f"{'-'*70}")
            else:
                print("No existen notas para ese usuario")
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            #Agregar codigo
            registro = nota.cambiar(usuario_id)
            if registro:
                print("Registro actualizado correctamente")
            else:
                print("No se pudo actualizar...")
            funciones.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            #Agregar codigo
            respuesta = nota.borrar(usuario_id)
            if respuesta:
                print("Se ha eliminado correctamente")
            else:
                print("No se ha eliminado")
            funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


