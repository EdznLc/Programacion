def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t\t🔃 Oprima cualquier tecla para continuar ...")

def menu_principlal():
    print("\n\t\t..::: Sistema de Gestión de Agenda de Contactos :::.." \
    "\n\n\t\t\t1️⃣  Agregar Contacto " \
    "\n\t\t\t2️⃣​  Mostrar todos los contactos " \
    "\n\t\t\t3️⃣​  Buscar contacto por nombre " \
    "\n\t\t\t4️⃣​  Modificar contacto " \
    "\n\t\t\t5️⃣​  Eliminar contacto " \
    "\n\t\t\t6️⃣​  SALIR ")
    opcion=input("\n\t\t\t👉 ​Elige una opción (1-6): ").upper()
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::📑​ Agregar Contacto 📑​::.")
    nombre=input("\n\t\t.::🧑​ Nombre del Contacto : ").upper().strip()
    if nombre in agenda:
        print("\n\t\t🚫 El contacto ya existe. No se puede agregar.")
    else:
        telefono=input("\t\t📞 Telefono: ").strip()
        email=input("\t\t📧 Email: ").lower().strip()
        #Agregar el atributo "nombre" al diccionario con los valores de telefono y email
        agenda[nombre] = [telefono, email]
        print("\n\t\t✔️ Contacto agregado con éxito ✔️")


def mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t.::🔎​ Mostrar Contactos 🔎​::.\n")
    if not agenda:
        print("\t\t🚫 No hay contactos en la agenda.")
    else:
        print(f"\t\t{'Nombre':<20}{'Telefono':<15}{'Email':<30}")
        print(f"\t\t{'-' * 65}")
    for nombre,datos in agenda.items():
        telefono, email = datos
        print(f"\t\t{nombre:<20}{telefono:<15}{email:<30}")
    print("\n\t\t✔️ Contactos mostrados con éxito ✔️")

def buscar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::🔍 Buscar Contacto 🔍::.")
    nombre=input("\n\t\t🧑 Nombre del Contacto a buscar: ").upper().strip()
    if nombre in agenda:
        telefono, email = agenda[nombre]
        print(f"\n\t\tContacto encontrado: {nombre} - Telefono: {telefono}, Email: {email}")
    else:
        print("\n\t\t🚫 El contacto no existe en la agenda.")
    print("\n\t\t✔️ Búsqueda completada ✔️")

def modificar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::✏️ Modificar Contacto ✏️::.")
    nombre=input("\n\t\t🧑 Nombre del Contacto a modificar: ").upper().strip()
    if nombre in agenda:
        telefono=input("\t\t📞 Nuevo Telefono: ").strip()
        email=input("\t\t📧 Nuevo Email: ").lower().strip()
        agenda[nombre] = [telefono, email]
        print("\n\t\t✔️ Contacto modificado con éxito ✔️")
    else:
        print("\n\t\t🚫 El contacto no existe en la agenda.")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::🗑️ Eliminar Contacto 🗑️::.")
    nombre=input("\n\t\t🧑 Nombre del Contacto a eliminar: ").upper().strip()
    if nombre in agenda:
        opcion=input("\n\t\t¿Estás seguro de que deseas eliminar este contacto? (S/N): ").upper().strip()
        if opcion == 'S':
            del agenda[nombre]
            print("\n\t\t✔️ Contacto eliminado con éxito ✔️")
        else:
            print("\n\t\t🚫 Eliminación cancelada.")
    else:
        print("\n\t\t🚫 El contacto no existe en la agenda.")