
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t\t🔃 Oprima cualquier tecla para continuar ...")

def menu_principlal():
    print("\n\t\t..::: Sistema de Gestión de Calificaciones :::...\n\n\t\t\t1️  Agregar Calificaciones  \n\t\t\t2️⃣​  Mostrar Calificaciones \n\t\t\t3️⃣​  Calcular el promedio\n\t\t\t5️⃣​  SALIR ")
    opcion=input("\n\t\t\t👉 ​Elige una opción (1-5): ").upper()
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    print("\n\t\t\t.::📑​ Agregar Calificaciones 📑​::.")
    nombre=input("\n\t\t\t.::🧑​ Nombre del Alumno : ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"\t\t\t🧾 Calificaion {i}: "))
                if cal>=0 and cal<=10:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("\n\t\t\t.::🚫Ingresa un numero valido🚫::.")
            except ValueError:
                print(".::🚫Ingresa un valor numerico🚫::.")
    lista.append([nombre]+calificaciones)
    print("\n\t\t\t.:: ✔️  Accion realizada con exito  ✔️ ::.")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("\n\t\t\t.::🔎​ Mostrar Calificaciones 🔎​::.\n")
    if len(lista)>0:
        print(f"\t\t\t{'Nombre':<15}{'Cal.1':<10}{'Cal.2':<10}{'Cal.3':<10}")
        print(f"\t\t\t{'-' * 40}")
        for fila in lista:
            print(f"\t\t\t{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
            print(f"\t\t\t{'-' * 40}")
        cuantos=len(lista)
        print(f"\t\t\tSon {cuantos} alumnos")
    else:
        print("\t\t\t.::🚫No existen calificaciones en el sistema🚫::.")

def calcular_promedios(lista):
    borrarPantalla()
    print("\n\t\t\t\t.:: 🧮​ Calcular Promedios🧮​ ::..")
    promedios=0
    promedio=0
    if len(lista) > 0:
        print(f"\t\t\t\t{'Nombre':<15}{'Promedio':<10}")
        print(f"\t\t\t\t{'-' * 30}")
        for fila in lista:
            promedio = sum(fila[1:])/3
            promedios+=promedio
            print(f"\t\t\t\t{fila[0]:<16}{promedio:<.2f}")
        print(f"\t\t\t\t{'-' * 30}")
        print(f"\n\t\t\t 😎 El promedio de los {len(lista)} alumnos es: {promedios/len(lista):.2f}")
    else:
        print("\t\t\t.::🚫No existen calificaciones en el sistema🚫::.")

def calcular_promedios2(lista):
    borrarPantalla()
    print("Calcular Promedios")
    promedios=0
    if len(lista) > 0:
        print(f"{'Nombre':<15}{'Promedio':<10}")
        print("-"*25)
        for fila in lista:
            i=0
            promedio=0
            suma=0
            while i<=3:
                suma+=fila[i]
                i+=1
            promedio = suma/3
            promedios+=promedio
            print(f"{fila[0]:<16}{promedio:<.2f}")
        print("-"*25)
        print(f"El promedio de los {len(lista)} alumnos es: {promedios/len(lista):.2f}")
    else:
        print("No hay datos para calcular promedios.")

def calcular_promedios3(lista):
    borrarPantalla()
    print("Calcular Promedios")
    promedios=0
    promedio=0
    if len(lista) > 0:
        print(f"{'Nombre':<15}{'Promedio':<10}")
        print("-"*25)
        for fila in lista:
            promedio = (fila[1] + fila[2] + fila[3]) / 3
            promedios+=promedio
            print(f"{fila[0]:<16}{promedio:<.2f}")
        print("-"*25)
        print(f"El promedio de los {len(lista)} alumnos es: {promedios/len(lista):.2f}")
    else:
        print("No hay datos para calcular promedios.")

def buscarAlumno(lista):
    contador=0
    borrarPantalla()
    nombre=input("Ingresa el nombre del alumno: ").upper().strip()
    print("Nombre Ca1 Cal2 Cal 3")
    for i in range(0,len(lista)):
        if lista[i][0]==nombre:
            print(f"{lista[i][0]}\t{lista[i][1]}\t{lista[i][2]}\t{lista[i][3]}")
            contador+=1
    if contador == 0:
        print("❌ No hay coincidencias")
    else:
        print(f"✅ Hay {contador} alumno(s) encontrados")
    input("Presione una tecla para continuar…")