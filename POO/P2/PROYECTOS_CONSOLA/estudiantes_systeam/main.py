from estudiante import estudiante
import os

class App:
    def __init__(self):
        self.main()

    def borrar_pantalla(self):
        os.system("cls")

    def esperar_tecla(self):
        input("Presione una tecla para continuar")

    def datos_estudiante(self, tipo):
        self.borrar_pantalla()
        print(f"Ingresa los datos del alumno de tipo {tipo}")
        nombre = input("Nombre: ")
        nota = input("Nota: ")
        return nombre, nota

    def menu_acciones(self, tipo):
        print(f"\n\t\t..::Menu de {tipo}::..\n\t1.-Insertar\n\t2.-Consultar\n\t3.-Actualizar\n\t4.-Eliminar\n\t5.-Regresar")
        opcion = input("\n\t\tElige una opcion: ").upper().strip()
        return opcion

    def respuesta_sql(self, respuesta):
        if respuesta:
            input("Accion realizada con exito")
        else:
            input("Algo ha salido mal")

    def menu_estudiante(self):
        while True:
            self.borrar_pantalla()
            opcion = self.menu_acciones("Alumnos")
            if opcion == "1":
                self.borrar_pantalla()
                nombre, nota = self.datos_estudiante("Alumno")
                respuesta = estudiante.Estudiante.insertar(nombre, nota)
                self.respuesta_sql(respuesta)
            elif opcion =="2":
                self.borrar_pantalla()
                alumnos = estudiante.Estudiante.consultar()
                if len(alumnos)>0:
                    for i in alumnos:
                        print(f"ID: {i[0]} | Nombre: {i[1]} | Nota: {float(i[2])}")
                    self.esperar_tecla()
                else:
                    print("No hay alumnos para mostrar")
                    self.esperar_tecla()
            elif opcion =="3":
                self.borrar_pantalla()
                nombre, nota = self.datos_estudiante("Alumno")
                id = input("Ingrese el id del estudiante: ")
                respuesta = estudiante.Estudiante.actualizar(nombre, nota, id)
                self.respuesta_sql(respuesta)
            elif opcion =="4":
                self.borrar_pantalla()
                id = input("Ingrese el id del estudiante: ")
                respuesta = estudiante.Estudiante.eliminar(id)
                self.respuesta_sql(respuesta)
            elif opcion =="5":
                break
            else:
                print("Opcion invalida")

    def main(self):
        opcion=True
        while opcion:
            self.borrar_pantalla()
            opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.-Alumnos\n\t2.-Salir\n\tElige un opción: ").lower().strip()
            match opcion:
                case "1":
                    self.menu_estudiante()
                    self.esperar_tecla()
                case "2":
                    self.borrar_pantalla()
                    input("\n\t\tSalir del Sistema")
                    opcion=False   
                case _:
                    input("Opcion invalida ... vuelva a intertarlo ... ")      


if __name__ == "__main__":
    app = App()