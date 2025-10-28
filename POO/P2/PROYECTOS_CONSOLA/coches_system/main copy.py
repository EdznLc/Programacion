# Main.py
# Sistema CRUD completo para vehículos
from model import coches, cochesBD
import os


# ------------------ Funciones generales ------------------

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\nPresione una tecla para continuar...")


def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t::: Ingresar datos del Vehículo tipo {tipo} :::\n")
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    velocidad = int(input("Velocidad: "))
    potencia = int(input("Potencia (caballaje): "))
    plazas = int(input("Número de plazas: "))
    return marca, color, modelo, velocidad, potencia, plazas


def resultado(res):
    print("\n✅ Operación exitosa." if res else "\n❌ Ocurrió un error.")


# ------------------ Función para mostrar registros ------------------

def mostrar_registros(lista, tipo):
    """Muestra los registros formateados en tabla."""
    borrarPantalla()
    print(f"\n\t::: LISTADO DE {tipo.upper()} :::\n")

    if not lista:
        print("No hay registros disponibles.")
        return

    # Determinar formato por tipo
    if tipo == "autos":
        print(f"{'ID':<5} {'Marca':<15} {'Color':<10} {'Modelo':<10} {'Velocidad':<10} {'Caballaje':<10} {'Plazas':<8}")
        print("-" * 70)
        for r in lista:
            print(f"{r[0]:<5} {r[1]:<15} {r[2]:<10} {r[3]:<10} {r[4]:<10} {r[5]:<10} {r[6]:<8}")

    elif tipo == "camionetas":
        print(f"{'ID':<5} {'Marca':<10} {'Color':<10} {'Modelo':<10} {'Velocidad':<10} {'Caballaje':<10} {'Plazas':<8} {'Tracción':<10} {'Cerrada':<10}")
        print("-" * 90)
        for r in lista:
            print(f"{r[0]:<5} {r[1]:<10} {r[2]:<10} {r[3]:<10} {r[4]:<10} {r[5]:<10} {r[6]:<8} {r[7]:<10} {str(r[8]):<10}")

    elif tipo == "camiones":
        print(f"{'ID':<5} {'Marca':<10} {'Color':<10} {'Modelo':<10} {'Velocidad':<10} {'Caballaje':<10} {'Plazas':<8} {'Ejes':<6} {'Capacidad':<10}")
        print("-" * 85)
        for r in lista:
            print(f"{r[0]:<5} {r[1]:<10} {r[2]:<10} {r[3]:<10} {r[4]:<10} {r[5]:<10} {r[6]:<8} {r[7]:<6} {r[8]:<10}")


# ------------------ CRUD AUTOS ------------------

def menu_autos():
    while True:
        borrarPantalla()
        print("\n\t::: MENÚ AUTOS :::")
        print("1.- Registrar auto")
        print("2.- Consultar autos")
        print("3.- Actualizar auto")
        print("4.- Eliminar auto")
        print("5.- Regresar al menú principal")
        op = input("\nSelecciona una opción: ").strip()

        match op:
            case "1":
                marca, color, modelo, velocidad, potencia, plazas = datos_autos("Auto")
                obj = cochesBD.Autos(marca, color, modelo, velocidad, potencia, plazas)
                resultado(obj.insertar())
                esperarTecla()
            case "2":
                mostrar_registros(cochesBD.Autos.consultar(), "autos")
                esperarTecla()
            case "3":
                registros = cochesBD.Autos.consultar()
                mostrar_registros(registros, "autos")
                if registros:
                    id = input("\nID del auto a actualizar: ")
                    marca, color, modelo, velocidad, potencia, plazas = datos_autos("Auto (nuevo)")
                    resultado(cochesBD.Autos.actualizar(marca, color, modelo, velocidad, potencia, plazas, id))
                esperarTecla()
            case "4":
                registros = cochesBD.Autos.consultar()
                mostrar_registros(registros, "autos")
                if registros:
                    id = input("\nID del auto a eliminar: ")
                    resultado(cochesBD.Autos.eliminar(id))
                esperarTecla()
            case "5":
                break
            case _:
                input("Opción inválida...")


# ------------------ CRUD CAMIONETAS ------------------

def menu_camionetas():
    while True:
        borrarPantalla()
        print("\n\t::: MENÚ CAMIONETAS :::")
        print("1.- Registrar camioneta")
        print("2.- Consultar camionetas")
        print("3.- Actualizar camioneta")
        print("4.- Eliminar camioneta")
        print("5.- Regresar al menú principal")
        op = input("\nSelecciona una opción: ").strip()

        match op:
            case "1":
                marca, color, modelo, velocidad, potencia, plazas = datos_autos("Camioneta")
                traccion = input("Tracción: ").upper()
                cerrada = input("¿Cerrada (SI/NO)?: ").strip().upper() == "SI"
                resultado(cochesBD.Camionetas.insertar(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada))
                esperarTecla()
            case "2":
                mostrar_registros(cochesBD.Camionetas.consultar(), "camionetas")
                esperarTecla()
            case "3":
                registros = cochesBD.Camionetas.consultar()
                mostrar_registros(registros, "camionetas")
                if registros:
                    id = input("\nID de la camioneta a actualizar: ")
                    marca, color, modelo, velocidad, potencia, plazas = datos_autos("Camioneta (nuevo)")
                    traccion = input("Tracción: ").upper()
                    cerrada = input("¿Cerrada (SI/NO)?: ").strip().upper() == "SI"
                    resultado(cochesBD.Camionetas.actualizar(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada, id))
                esperarTecla()
            case "4":
                registros = cochesBD.Camionetas.consultar()
                mostrar_registros(registros, "camionetas")
                if registros:
                    id = input("\nID de la camioneta a eliminar: ")
                    resultado(cochesBD.Camionetas.eliminar(id))
                esperarTecla()
            case "5":
                break
            case _:
                input("Opción inválida...")


# ------------------ CRUD CAMIONES ------------------

def menu_camiones():
    while True:
        borrarPantalla()
        print("\n\t::: MENÚ CAMIONES :::")
        print("1.- Registrar camión")
        print("2.- Consultar camiones")
        print("3.- Actualizar camión")
        print("4.- Eliminar camión")
        print("5.- Regresar al menú principal")
        op = input("\nSelecciona una opción: ").strip()

        match op:
            case "1":
                marca, color, modelo, velocidad, potencia, plazas = datos_autos("Camión")
                ejes = int(input("Número de ejes: "))
                capacidad = int(input("Capacidad de carga: "))
                resultado(cochesBD.Camion.insertar(marca, color, modelo, velocidad, potencia, plazas, ejes, capacidad))
                esperarTecla()
            case "2":
                mostrar_registros(cochesBD.Camion.consultar(), "camiones")
                esperarTecla()
            case "3":
                registros = cochesBD.Camion.consultar()
                mostrar_registros(registros, "camiones")
                if registros:
                    id = input("\nID del camión a actualizar: ")
                    marca, color, modelo, velocidad, potencia, plazas = datos_autos("Camión (nuevo)")
                    ejes = int(input("Número de ejes: "))
                    capacidad = int(input("Capacidad de carga: "))
                    resultado(cochesBD.Camion.actualizar(marca, color, modelo, velocidad, potencia, plazas, ejes, capacidad, id))
                esperarTecla()
            case "4":
                registros = cochesBD.Camion.consultar()
                mostrar_registros(registros, "camiones")
                if registros:
                    id = input("\nID del camión a eliminar: ")
                    resultado(cochesBD.Camion.eliminar(id))
                esperarTecla()
            case "5":
                break
            case _:
                input("Opción inválida...")


# ------------------ MENÚ PRINCIPAL ------------------

def main():
    opcion = ""
    while opcion != "4":
        borrarPantalla()
        print("\n\t\t::: SISTEMA DE VEHÍCULOS :::")
        print("1.- Autos")
        print("2.- Camionetas")
        print("3.- Camiones")
        print("4.- Salir")
        opcion = input("\nSelecciona una opción: ").strip()

        match opcion:
            case "1":
                menu_autos()
            case "2":
                menu_camionetas()
            case "3":
                menu_camiones()
            case "4":
                borrarPantalla()
                print("\nSaliendo del sistema...")
            case _:
                input("\nOpción inválida...")


if __name__ == "__main__":
    main()
