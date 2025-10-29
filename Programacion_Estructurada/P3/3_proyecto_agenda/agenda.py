import os
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # tu contraseña aquí
        database="bd_agenda"
    )

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t\t\t🔃 Oprima cualquier tecla para continuar ...")

def menu_principal():
    print("\n\t\t..::: Sistema de Gestión de Agenda de Contactos :::.." \
    "\n\n\t\t\t1️⃣  Agregar Contacto " \
    "\n\t\t\t2️⃣​  Mostrar todos los contactos " \
    "\n\t\t\t3️⃣​  Buscar contacto por nombre " \
    "\n\t\t\t4️⃣​  Modificar contacto " \
    "\n\t\t\t5️⃣​  Eliminar contacto " \
    "\n\t\t\t6️⃣​  SALIR ")
    return input("\n\t\t\t👉 ​Elige una opción (1-6): ").upper()

def agregar_contacto():
    borrarPantalla()
    print("\n\t\t.::📑​ Agregar Contacto 📑​::.")
    nombre = input("\n\t\t.::🧑​ Nombre del Contacto : ").upper().strip()
    telefono = input("\t\t📞 Teléfono: ").strip()
    email = input("\t\t📧 Email: ").lower().strip()

    con = conectar()
    cursor = con.cursor()

    try:
        cursor.execute("INSERT INTO contactos (nombre, telefono, email) VALUES (%s, %s, %s)", (nombre, telefono, email))
        con.commit()
        print("\n\t\t✔️ Contacto agregado con éxito ✔️")
    except mysql.connector.IntegrityError:
        print("\n\t\t🚫 El contacto ya existe. No se puede agregar.")
    finally:
        con.close()

def mostrar_contactos():
    borrarPantalla()
    print("\n\t\t.::🔎​ Mostrar Contactos 🔎​::.\n")
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id, nombre, telefono, email FROM contactos")
    registros = cursor.fetchall()
    con.close()

    if registros:
        print(f"\t\t{'ID':<5}{'Nombre':<20}{'Teléfono':<15}{'Email':<30}")
        print(f"\t\t{'-' * 70}")
        for fila in registros:
            print(f"\t\t{fila[0]:<5}{fila[1]:<20}{fila[2]:<15}{fila[3]:<30}")
        print("\n\t\t✔️ Contactos mostrados con éxito ✔️")
    else:
        print("\t\t🚫 No hay contactos en la agenda.")

def buscar_contacto():
    borrarPantalla()
    print("\n\t\t.::🔍 Buscar Contacto 🔍::.")
    nombre = input("\n\t\t🧑 Nombre del Contacto a buscar: ").upper().strip()
    
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id, nombre, telefono, email FROM contactos WHERE nombre = %s", (nombre,))
    registro = cursor.fetchone()
    con.close()

    if registro:
        print(f"\n\t\tContacto encontrado:")
        print(f"\t\tID: {registro[0]}, Nombre: {registro[1]}, Teléfono: {registro[2]}, Email: {registro[3]}")
    else:
        print("\n\t\t🚫 El contacto no existe en la agenda.")
    print("\n\t\t✔️ Búsqueda completada ✔️")

def modificar_contacto():
    borrarPantalla()
    print("\n\t\t.::✏️ Modificar Contacto ✏️::.")
    nombre = input("\n\t\t🧑 Nombre del Contacto a modificar: ").upper().strip()

    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id FROM contactos WHERE nombre = %s", (nombre,))
    resultado = cursor.fetchone()

    if resultado:
        telefono = input("\t\t📞 Nuevo Teléfono: ").strip()
        email = input("\t\t📧 Nuevo Email: ").lower().strip()
        cursor.execute("UPDATE contactos SET telefono = %s, email = %s WHERE nombre = %s", (telefono, email, nombre))
        con.commit()
        print("\n\t\t✔️ Contacto modificado con éxito ✔️")
    else:
        print("\n\t\t🚫 El contacto no existe en la agenda.")
    con.close()

def eliminar_contacto():
    borrarPantalla()
    print("\n\t\t.::🗑️ Eliminar Contacto 🗑️::.")
    nombre = input("\n\t\t🧑 Nombre del Contacto a eliminar: ").upper().strip()

    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id FROM contactos WHERE nombre = %s", (nombre,))
    resultado = cursor.fetchone()

    if resultado:
        opcion = input("\n\t\t¿Estás seguro de que deseas eliminar este contacto? (S/N): ").upper().strip()
        if opcion == 'S':
            cursor.execute("DELETE FROM contactos WHERE nombre = %s", (nombre,))
            con.commit()
            print("\n\t\t✔️ Contacto eliminado con éxito ✔️")
        else:
            print("\n\t\t🚫 Eliminación cancelada.")
    else:
        print("\n\t\t🚫 El contacto no existe en la agenda.")
    con.close()