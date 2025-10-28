#Instanciar los objetos para posterior implementarlos 
from model import coches, cochesBD
import os

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        os.system("cls")

    def esperarTecla(self):
        input("\n\t\tOprima una tecla para continuar:")

    def datos_autos(self, tipo):
        self.borrarPantalla()
        print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
        marca=input("Marca: ").upper()
        color=input("Color: ").upper()
        modelo=input("Modelo: ").upper()
        velocidad=int(input("Velocidad: "))
        potencia=int(input("Potencia: "))
        plazas=int(input("No. de plazas: "))
        return marca,color,modelo,velocidad,potencia,plazas

    def imprimir_datos_vehiculo(self,marca,color,modelo,velocidad,potencia,plazas):
        self.borrarPantalla()
        print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n Color: {color} \n Modelo: {modelo} \n Velocidad: {velocidad} \n Caballaje: {potencia} \n Plazas: {plazas}")

    def resultado(self,respuesta):
        if respuesta:
            print("Accion realizada con exito")
            self.esperarTecla()
        else:
            print("No fue posible realizar la accion")
            self.esperarTecla()

    def autos(self):
        marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Auto")
        coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
        self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
        self.esperarTecla()
        return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas


    def camionetas(self):
        marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Camioneta")
        traccion=input("Traccion: ").upper()
        cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
        if cerrada=="SI":
            cerrada=True
        else:
            cerrada=False    
        coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
        self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
        print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")
        self.esperarTecla()
        return coche.marca, coche.color, coche.modelo, coche.velocidad, coche.caballaje, coche.plazas, coche.traccion, coche.cerrada

    def camiones(self):
        marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Camiones")
        eje=int(input("No. de ejes: "))
        capacidadCarga=int(input("Capacidad de carga: "))
        coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
        self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
        print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")
        return coche.marca, coche.color, coche.modelo, coche.velocidad, coche.caballaje, coche.plazas, coche.eje, coche.capacidadCarga

    def menu_acciones(self,tipo):
        print(f"\n\t\t..::Menu de {tipo}::..\n\t1.-Instertar\n\t2.-Consultar\n\t3.-Actualizar\n\t4.-Eliminar\n\t5.-Regresar")
        opcion = input("\n\t\tElige una opcion: ").upper().strip()
        return opcion

    def menu_autos(self):
        while True:
            self.borrarPantalla()
            op = self.menu_acciones("Autos")
            if op == "1" or op == "INSERTAR":
                marca, color, modelo, velocidad, caballaje, plazas = self.autos()
                #Acceder a la BD
                auto = cochesBD.Autos(marca, color, modelo, velocidad, caballaje, plazas)
                respuesta = auto.insertar()
                self.resultado(respuesta)
            elif op == "2" or op == "CONSULTAR":
                self.borrarPantalla()
                num_auto = 1
                registros = cochesBD.Autos.consultar()
                if len(registros)>0:
                    for i in registros:
                        print(f"Auto # {num_auto} con ID: {i[0]}\nMarca: {i[1]}\nColor: {i[2]}\nModelo: {i[3]}\nVelocidad: {i[4]}\nPotencia: {i[5]}\nPlazas: {i[6]}")
                        num_auto += 1
                        self.esperarTecla()
                else:
                    print("No hay datos para mostrar")
                    self.esperarTecla()
                print("Consultar")
            elif op == "3" or op == "ACTUALIZAR":
                self.borrarPantalla()
                id = input("Ingrese el ID a actualizar: ").strip()
                marca, color, modelo, velocidad, caballaje, plazas = self.autos()
                respuesta = cochesBD.Autos.actualizar(marca, color, modelo, velocidad, caballaje, plazas, id)
                self.resultado(respuesta)
            elif op == "4" or op == "ELIMINAR":
                self.borrarPantalla()
                id = input("Ingrese el ID a eliminar: ").strip()
                respuesta = cochesBD.Autos.eliminar(id)
                self.resultado(respuesta)
            elif op == "5" or op == "REGRESAR":
                break
            else:
                print("Opcion no valida")
                self.esperarTecla()

    def menu_camionetas(self):
        while True:
            self.borrarPantalla()
            op = self.menu_acciones("Camionetas")
            if op == "1" or op == "INSERTAR":
                marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada = self.camionetas()
                #Acceder a la BD
                respuesta = cochesBD.Camionetas.insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion,  cerrada)
                self.resultado(respuesta)
            elif op == "2" or op == "CONSULTAR":
                self.borrarPantalla()
                num_auto = 1
                registros = cochesBD.Camionetas.consultar()
                if len(registros)>0:
                    for i in registros:
                        print(f"Camioneta # {num_auto} con ID: {i[0]}\nMarca: {i[1]}\nColor: {i[2]}\nModelo: {i[3]}\nVelocidad: {i[4]}\nPotencia: {i[5]}\nPlazas: {i[6]}\nTraccion: {i[7]}\nCerrada: {i[8]}")
                        num_auto += 1
                        self.esperarTecla()
                else:
                    print("No hay datos para mostrar")
                    self.esperarTecla()
                print("Consultar")
            elif op == "3" or op == "ACTUALIZAR":
                self.borrarPantalla()
                id = input("Ingrese el ID a actualizar: ").strip()
                marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada = self.camionetas()
                respuesta = cochesBD.Camionetas.actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id)
                self.resultado(respuesta)
            elif op == "4" or op == "ELIMINAR":
                self.borrarPantalla()
                id = input("Ingrese el ID a eliminar: ").strip()
                respuesta = cochesBD.Camionetas.eliminar(id)
                self.resultado(respuesta)
            elif op == "5" or op == "REGRESAR":
                break
            else:
                print("Opcion no valida")
                self.esperarTecla()

    def menu_camiones(self):
        while True:
            self.borrarPantalla()
            op = self.menu_acciones("Camiones")
            if op == "1" or op == "INSERTAR":
                marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga = self.camiones()
                #Acceder a la BD
                respuesta = cochesBD.Camion.insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga)
                self.resultado(respuesta)
            elif op == "2" or op == "CONSULTAR":
                self.borrarPantalla()
                num_auto = 1
                registros = cochesBD.Camion.consultar()
                if len(registros)>0:
                    for i in registros:
                        print(f"Camiones # {num_auto} con ID: {i[0]}\nMarca: {i[1]}\nColor: {i[2]}\nModelo: {i[3]}\nVelocidad: {i[4]}\nPotencia: {i[5]}\nPlazas: {i[6]}\nEjes: {i[7]}\nCapacidad Carga: {i[8]}")
                        num_auto += 1
                        self.esperarTecla()
                else:
                    print("No hay datos para mostrar")
                    self.esperarTecla()
                print("Consultar")
            elif op == "3" or op == "ACTUALIZAR":
                self.borrarPantalla()
                id = input("Ingrese el ID a actualizar: ").strip()
                marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga = self.camiones()
                respuesta = cochesBD.Camion.actualizar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id)
                self.resultado(respuesta)
            elif op == "4" or op == "ELIMINAR":
                self.borrarPantalla()
                id = input("Ingrese el ID a eliminar: ").strip()
                respuesta = cochesBD.Camion.eliminar(id)
                self.resultado(respuesta)
            elif op == "5" or op == "REGRESAR":
                break
            else:
                print("Opcion no valida")
                self.esperarTecla()


    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.-Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
            match opcion:
                case "1":
                    self.menu_autos()
                    self.esperarTecla()
                case "2":
                    self.menu_camionetas()
                    self.esperarTecla()  
                case "3":
                    self.menu_camiones()
                    self.esperarTecla()
                case "4":
                    self.borrarPantalla()
                    input("\n\t\tSalir del Sistema")
                    opcion=False   
                case _:
                    input("Opcion invalida ... vuelva a intertarlo ... ")      

if __name__=="__main__":
    app = App()