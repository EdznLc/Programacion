from usuarios import usuarioBD
from notas import notaBD
from funciones import *
import getpass

class App:
    def __init__(self):
        self.menu_principal()
    
    def menu_principal(self):
        while True:
            borrarPantalla()
            print("""
            .::  Menu Principal ::. 
            1.- Registro
            2.- Login
            3.- Salir 
            """)
            opcion = input("\t Elige una opción: ").upper().strip()

            if opcion in ("1", "REGISTRO"):
                borrarPantalla()
                print("\n \t ..:: Registro en el Sistema ::..")
                nombre = input("\t ¿Cuál es tu nombre?: ")
                apellidos = input("\t ¿Cuáles son tus apellidos?: ")
                email = input("\t Ingresa tu email: ")
                contrasena = getpass.getpass("\t Ingresa tu contraseña: ")

                usuario = usuarioBD.Usuario.registrar(nombre, apellidos, email, contrasena)
                resultado = usuario.registrar()

                if resultado:
                    print(f"\n\t {nombre} {apellidos}, se registró correctamente con el email: {email}")
                else:
                    print(f"\n\t ** No fue posible registrar el usuario **")
                esperarTecla()

            elif opcion in ("2", "LOGIN"):
                borrarPantalla()
                print("\n \t ..:: Inicio de Sesión ::.. ")     
                email = input("\t Ingresa tu E-mail: ")
                contrasena = getpass.getpass("\t Ingresa tu Contraseña: ")
                registro = usuarioBD.Usuario.iniciar_sesion(email, contrasena)

                if registro:
                    self.menu_notas(registro[0], registro[1], registro[2])
                else:
                    print(f"\n\t Email y/o contraseña incorrectas... vuelva a intentarlo ...")
                    esperarTecla()

            elif opcion in ("3", "SALIR"):
                print("\n\t.. ¡Gracias! Bye ...")
                break
            else:
                print("\n \t Opción no válida. Intenta de nuevo.")
                esperarTecla()

    def menu_notas(self,usuario_id, nombre, apellidos):
        while True:
            borrarPantalla()
            print(f"\nBienvenido {nombre} {apellidos}, has iniciado sesión...")
            print("""
            .::  Menu Notas ::. 
            1.- Crear 
            2.- Mostrar
            3.- Cambiar
            4.- Eliminar
            5.- Salir 
            """)
            opcion = input("\t\t Elige una opción: ").upper().strip()

            if opcion in ("1", "CREAR"):
                borrarPantalla()
                print(f"\n .:: Crear Nota ::. ")
                titulo = input("\t Título: ")
                descripcion = input("\t Descripción: ")

                nota = notaBD.Nota.crear(usuario_id, titulo, descripcion)
                resultado = nota.crear()

                if resultado:
                    print(f"\n La nota '{titulo}' se creó correctamente.")
                else:
                    print(f"\n ** No fue posible crear la nota **")
                esperarTecla()

            elif opcion in ("2", "MOSTRAR"):
                borrarPantalla()
                registros = notaBD.Nota.mostrar(usuario_id)
                if registros:
                    print(f"\nNotas de {nombre} {apellidos}:")
                    for i, fila in enumerate(registros, start=1):
                        print(f"\nNota #{i} | ID: {fila[0]} | Título: {fila[2]} | Fecha: {fila[4]}")
                        print(f"Descripción: {fila[3]}")
                else:
                    print(f"\n ** No existen notas para este usuario **")
                esperarTecla()

            elif opcion in ("3", "CAMBIAR"):
                borrarPantalla()
                id = input("ID de la nota a actualizar: ")
                titulo = input("Nuevo título: ")
                descripcion = input("Nueva descripción: ")

                resultado = notaBD.Nota.actualizar(titulo, descripcion, id)
                print("\nNota actualizada correctamente." if resultado else "\n** No fue posible actualizar la nota **")
                esperarTecla()

            elif opcion in ("4", "ELIMINAR"):
                borrarPantalla()
                id = input("ID de la nota a eliminar: ")
                resultado = notaBD.Nota.eliminar(id)
                print("\nNota eliminada correctamente." if resultado else "\n** No fue posible eliminar la nota **")
                esperarTecla()

            elif opcion in ("5", "SALIR"):
                break
            else:
                print("\n Opción no válida.")
                esperarTecla()


if __name__ == "__main__":
    app = App()
