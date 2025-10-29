
import os
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # tu contraseña
        database="bd_calificaciones"
    )

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\n\t\t\t🔃 Oprima cualquier tecla para continuar ...")

def agregar_calificaciones():
    borrarPantalla()
    print("\n\t\t\t.::📑​ Agregar Calificaciones 📑​::.")
    nombre = input("\n\t\t\t.::🧑​ Nombre del Alumno : ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        while True:
            try:
                cal = float(input(f"\t\t\t🧾 Calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    break
                else:
                    print("\n\t\t\t.::🚫Ingresa un número válido (0-10)🚫::.")    
            except ValueError:
                print("\t\t\t.::🚫 Ingresa un valor numérico 🚫::.")

    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO alumnos (nombre, cal1, cal2, cal3) VALUES (%s, %s, %s, %s)",(nombre, calificaciones[0], calificaciones[1], calificaciones[2]))
    con.commit()
    con.close()
    print("\n\t\t\t.:: ✔️  Acción realizada con éxito ✔️ ::.")

def mostrar_calificaciones():
    borrarPantalla()
    print("\n\t\t\t.::🔎​ Mostrar Calificaciones 🔎​::.\n")
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id, nombre, cal1, cal2, cal3 FROM alumnos")
    registros = cursor.fetchall()
    con.close()

    if registros:
        print(f"\t\t\t{'ID':<5}{'Nombre':<15}{'Cal.1':<10}{'Cal.2':<10}{'Cal.3':<10}")
        print(f"\t\t\t{'-' * 50}")
        for fila in registros:
            print(f"\t\t\t{fila[0]:<5}{fila[1]:<15}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
            print(f"\t\t\t{'-' * 50}")
        print(f"\t\t\tSon {len(registros)} alumno(s)")
    else:
        print("\t\t\t.::🚫No existen calificaciones en el sistema🚫::.")

def calcular_promedios():
    borrarPantalla()
    print("\n\t\t\t.:: 🧮 Calcular Promedios 🧮 ::.\n")
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id, nombre, cal1, cal2, cal3 FROM alumnos")
    registros = cursor.fetchall()
    con.close()

    if registros:
        total_promedios = 0
        print(f"\t\t\t{'ID':<5}{'Nombre':<15}{'Promedio':<10}")
        print(f"\t\t\t{'-' * 35}")
        for fila in registros:
            promedio = sum(fila[2:]) / 3
            total_promedios += promedio
            print(f"\t\t\t{fila[0]:<5}{fila[1]:<15}{promedio:.2f}")
        print(f"\t\t\t{'-' * 35}")
        print(f"\n\t\t\t😎 El promedio general es: {total_promedios/len(registros):.2f}")
    else:
        print("\t\t\t.::🚫No hay datos para calcular promedios🚫::.")

def buscarAlumno():
    borrarPantalla()
    nombre = input("\n\t\t\t🔍 Ingresa el nombre del alumno: ").upper().strip()
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id, nombre, cal1, cal2, cal3 FROM alumnos WHERE nombre = %s", (nombre,))
    registros = cursor.fetchall()
    con.close()

    if registros:
        print(f"\t\t\t{'ID':<5}{'Nombre':<15}{'Cal.1':<10}{'Cal.2':<10}{'Cal.3':<10}")
        print(f"\t\t\t{'-' * 50}")
        for fila in registros:
            print(f"\t\t\t{fila[0]:<5}{fila[1]:<15}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
        print(f"\t\t\t✅ Alumno(s) encontrado(s): {len(registros)}")
    else:
        print("\t\t\t❌ No hay coincidencias")

def menu_principlal():
    print("\n\t\t..::: Sistema de Gestión de Calificaciones :::...\n\n\t\t\t1️  Agregar Calificaciones  \n\t\t\t2️⃣​  Mostrar Calificaciones \n\t\t\t3️⃣​  Calcular el promedio \n\t\t\t 4️⃣​  Buscar Alumno  \n\t\t\t5️⃣​  SALIR ")
    opcion=input("\n\t\t\t👉 ​Elige una opción (1-4): ").upper()
    return opcion