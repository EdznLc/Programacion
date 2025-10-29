from conexion import *

def check_id_cliente(id_cliente):
    try:
        cursor.execute(
            "select * from clientes where id=%s",(id_cliente,)
        )
        registro=cursor.fetchone()
        if registro:
            return True 
        else:
            return None
    except:
        return None

def check_id_usuario(id_usuario):
    try:
        cursor.execute(
            "select * from usuarios where id=%s",(id_usuario,)
        )
        registro=cursor.fetchone()
        if registro:
            return True 
        else:
            return None
    except:
        return None

def crear(usuario_id,nombre,tel,direccion,correo,edad):
    try:
        cursor.execute(
            "insert into clientes (id_usuario,nombre,telefono,direccion,correo,edad) values (%s,%s,%s,%s,%s,%s)",(usuario_id,nombre,tel,direccion,correo,edad)
        )
        conexion.commit()
        return True
    except:
        return None
    

def consultar(id_cliente):
    try:
        cursor.execute("select * from clientes where id=%s", (id_cliente,))
        registro = cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return None
    

def actualizar(usuario_id):
    try:
        cursor.execute("SELECT * FROM clientes")
        registros = cursor.fetchall()
        if registros:
            print(f"+{'-'*5}+{'-'*22}+{'-'*22}+{'-'*17}+{'-'*27}+{'-'*27}+{'-'*6}+")
            print(f"| {'ID':<3} | {'Usuario ID':<20} | {'Nombre':<20} | {'Teléfono':<15} | {'Dirección':<25} | {'Correo':<25} | {'Edad':<4} |")
            print(f"+{'-'*5}+{'-'*22}+{'-'*22}+{'-'*17}+{'-'*27}+{'-'*27}+{'-'*6}+")
            for fila in registros:
                print(f"| {fila[0]:<3} | {fila[1]:<20} | {fila[2]:<20} | {fila[3]:<15} | {fila[4]:<25} | {fila[5]:<25} | {fila[6]:<4} |")
                print(f"+{'-'*5}+{'-'*22}+{'-'*22}+{'-'*17}+{'-'*27}+{'-'*27}+{'-'*6}+")
            op = input("¿Desea actualizar algún cliente? (S/N): ").strip().upper()
            if op != 'S':
                print("⚠️  Operacion cancelada  ⚠️")
                return None
            id_cliente = input("Ingrese el ID del cliente a actualizar: ").strip()
            if not check_id_cliente(id_cliente):
                print("❌ El cliente no existe.")
                return None
            nombre = input("Nuevo Nombre: ").strip().upper()
            while True:
                tel = input("Nuevo Teléfono: ").strip()
                if tel.isdigit():
                    break
                else:
                    print("⚠️  Solo valores numericos  ⚠️")
            direccion = input("Nueva Dirección: ").strip().upper()
            correo = input("Nuevo Correo: ").strip().lower()
            while True:
                edad = input("Nueva Edad: ").strip()
                if edad.isdigit():
                    break
                else:
                    print("⚠️  Solo valores numericos  ⚠️")
            cursor.execute("UPDATE clientes SET id_usuario=%s, nombre=%s, telefono=%s, direccion=%s, correo=%s, edad=%s WHERE id=%s", (usuario_id,nombre, tel, direccion, correo, edad, id_cliente))
            conexion.commit()
            print(f"✅ Cliente {id_cliente} actualizado correctamente.")
            return True
        else:
            print("\t\t\t⚠️  No hay clientes registrados.  ⚠️")
            return None
    except Exception as e:
        print(f"⚠️  Ocurrió un error, revise que sus datos sean correctos  ⚠️")
        return None

def borrar():
    try:
        cursor.execute("SELECT * FROM clientes")
        registros = cursor.fetchall()
        if registros:
            print(f"+{'-'*5}+{'-'*22}+{'-'*22}+{'-'*17}+{'-'*27}+{'-'*27}+{'-'*6}+")
            print(f"| {'ID':<3} | {'Usuario ID':<20} | {'Nombre':<20} | {'Teléfono':<15} | {'Dirección':<25} | {'Correo':<25} | {'Edad':<4} |")
            print(f"+{'-'*5}+{'-'*22}+{'-'*22}+{'-'*17}+{'-'*27}+{'-'*27}+{'-'*6}+")
            for fila in registros:
                print(f"| {fila[0]:<3} | {fila[1]:<20} | {fila[2]:<20} | {fila[3]:<15} | {fila[4]:<25} | {fila[5]:<25} | {fila[6]:<4} |")
                print(f"+{'-'*5}+{'-'*22}+{'-'*22}+{'-'*17}+{'-'*27}+{'-'*27}+{'-'*6}+")
            op = input("¿Desea eliminar algún cliente? (S/N): ").strip().upper()
            if op == 'S':
                id_cliente = input("Ingrese el ID del cliente a eliminar: ").strip()
                existe = check_id_cliente(id_cliente)
                if not existe:
                    print("⚠️  El cliente no existe.  ⚠️")
                    return None
                opcion = input(f"¿Seguro que desea eliminar el cliente {id_cliente}? (S/N): ").strip().upper()
                if opcion == 'S':
                    cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
                    conexion.commit()
                    return id_cliente
                else:
                    print("⚠️  Operación cancelada.  ⚠️")
                    return None
            else:
                print("⚠️  Operación cancelada.  ⚠️")
                return None
        else:
            print("\t\t\t⚠️  No hay clientes registrados.  ⚠️")
            return None
    except Exception as e:
        print(f"⚠️  Ocurrió un error: {e}  ⚠️")
        return None

def listar():
    try:
        cursor.execute("SELECT * FROM clientes")
        registros = cursor.fetchall()
        if registros:
            return registros
        else:
            print("\t\t\t⚠️  No hay clientes registrados.  ⚠️")
            return None
    except Exception as e:
        print(f"⚠️  Ocurrió un error: {e}  ⚠️")
        return None


