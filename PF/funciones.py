import os

class Funciones:
    
    @staticmethod
    def borrarPantalla():
        os.system("cls" if os.name == 'nt' else 'clear')

    @staticmethod
    def esperarTecla():
        input("\n\t\t\t🔃 Oprima cualquier tecla para continuar ...")

    @staticmethod
    def menu_principal():
        print("\n\t\t..::: Sistema de Gestión de Ropa :::...")
        print(
        "\n\t\t\t1️⃣  Registro " \
        "\n\t\t\t2️⃣​  Login " \
        "\n\t\t\t3️⃣​  SALIR ")
        opcion=input("\n\t\t\t👉 ​Elige una opción: ").upper().strip()
        return opcion

    @staticmethod
    def menu_clientes():
        print("\n\t\t..::: Clientes :::... \n" \
        "\n\t\t1️⃣  Crear Cliente  " \
        "\n\t\t2️⃣​  Consultar Cliente " \
        "\n\t\t3️⃣​  Actualizar Cliente " \
        "\n\t\t4️⃣​  Eliminar Cliente " \
        "\n\t\t5️⃣​  Listar Clientes " \
        "\n\t\t6️⃣  Exportar " \
        "\n\t\t7️⃣  Salir ")
        
        opcion=input("\n\t\t👉 ​Elige una opción: ").upper().strip()
        return opcion

    @staticmethod
    def menu_ventas():
        print("\n\t\t..::: Ventas :::...\n" \
        "\n\t\t1️⃣  Crear Ventas " \
        "\n\t\t2️⃣​  Consultar Ventas " \
        "\n\t\t3️⃣​  Actualizar Ventas " \
        "\n\t\t4️⃣​  Eliminar Ventas " \
        "\n\t\t5️⃣​  Listar Ventas " \
        "\n\t\t6️⃣  Exportar " \
        "\n\t\t7️⃣  Salir ")
        opcion=input("\n\t\t👉 ​Elige una opción: ").upper().strip()
        return opcion