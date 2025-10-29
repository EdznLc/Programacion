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

def check_id_venta(id_venta):
    try:
        cursor.execute(
            "select * from ventas where id=%s",(id_venta,)
        )
        registro=cursor.fetchone()
        if registro:
            return True 
        else:
            return None
    except:
        return None

def imprimir_tabla_ventas(registros):
    print(f"+{'-'*5}+{'-'*12}+{'-'*13}+{'-'*10}+{'-'*15}+{'-'*20}+{'-'*12}+")
    print(f"| {'ID':<3} | {'ID Usuario':<10} | {'ID Cliente':<11} | {'Monto':<8} | {'# Prendas':<13} | {'Método de Pago':<18} | {'Fecha':<10} |")
    print(f"+{'-'*5}+{'-'*12}+{'-'*13}+{'-'*10}+{'-'*15}+{'-'*20}+{'-'*12}+")
    for venta in registros:
        print(f"| {venta[0]:<3} | {venta[1]:<10} | {venta[2]:<11} | {venta[3]:<8.2f} | {venta[4]:<13} | {venta[5]:<18} | {str(venta[6]):<10} |")
        print(f"+{'-'*5}+{'-'*12}+{'-'*13}+{'-'*10}+{'-'*15}+{'-'*20}+{'-'*12}+")

def crear(usuario_id,id_cliente,monto,nprendas,metodopago):
    try:
        cursor.execute(
            "insert into ventas (id_usuario, id_cliente, monto, num_prendas, metodo_pago, fecha) values (%s,%s,%s,%s,%s,NOW())",(usuario_id,id_cliente,monto,nprendas,metodopago)
        )
        conexion.commit()
        return True
    except:
        return None
    

def consultar(id_venta):
    try:
        cursor.execute("select * from ventas where id=%s", (id_venta,))
        registro = cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return None
    

def actualizar(usuario_id):
    try:
        cursor.execute("SELECT * FROM ventas")
        registros = cursor.fetchall()
        if registros:
            imprimir_tabla_ventas(registros)
            op = input("¿Desea actualizar algúna venta? (S/N): ").strip().upper()
            if op != 'S':
                print("⚠️  Operacion cancelada  ⚠️")
                return None
            id_venta = input("Ingrese el ID de la venta a actualizar: ").strip()
            if not check_id_venta(id_venta):
                print("❌ La venta no existe.")
                return None
            id_cliente = input("Ingrese el ID de cliente: ").strip()
            if not check_id_cliente(id_cliente):
                print("❌ El cliente no existe.")
                return None
            while True:
                monto = input("Monto: ")
                try:
                    monto_float = float(monto)
                    monto = monto_float
                    break
                except ValueError:
                    print("\t⚠️  Solo valores numéricos  ⚠️")
            while True:
                nprendas = input("Ingrese el nuevo número de prendas: ").strip()
                if nprendas.isdigit():
                    break
                else:
                    print("⚠️  Solo valores numericos  ⚠️")
            while True:
                metodopago = input("Ingrese el nuevo método de pago: ").strip()
                if metodopago=="e":
                    metodopago="EFECTIVO"
                    break
                elif metodopago=="t":
                    metodopago="TRANSFERENCIA"
                    break
                else:
                    print("\t⚠️  Solo Efectivo=E/Transfrenecia=T  ⚠️")
            cursor.execute("UPDATE ventas SET id_usuario=%s, id_cliente=%s, monto=%s, num_prendas=%s, metodo_pago=%s WHERE id=%s",(usuario_id, id_cliente, monto, nprendas, metodopago, id_venta))
            conexion.commit()
            return id_venta
        else:
            print("\t\t\t⚠️  No hay ventas registradas.  ⚠️")
            return None
    except Exception as e:
        print(f"⚠️  Ocurrió un error: {e}  ⚠️")
        return None

def borrar():
    try:
        cursor.execute("SELECT * FROM ventas")
        registros = cursor.fetchall()
        if registros:
            imprimir_tabla_ventas(registros)
            print("\n\t\t..::: Eliminar Ventas :::...")
            op = input("¿Desea eliminar algúna venta? (S/N): ").strip().upper()
            if op == 'S':
                id_venta = input("Ingrese el ID de la venta a eliminar: ").strip()
                existe = check_id_venta(id_venta)
                if not existe:
                    print("⚠️  La venta no existe.  ⚠️")
                    return None
                opcion = input(f"¿Seguro que desea eliminar la venta {id_venta}? (S/N): ").strip().upper()
                if opcion == 'S':
                    cursor.execute("DELETE FROM ventas WHERE id = %s", (id_venta,))
                    conexion.commit()
                    return id_venta
                else:
                    print("⚠️  Operación cancelada.  ⚠️")
                    return None
            else:
                print("⚠️  Operación cancelada.  ⚠️")
                return None
        else:
            print("\t\t\t⚠️  No hay ventas registradas.  ⚠️")
            return None
    except Exception as e:
        print(f"⚠️  Ocurrió un error: {e}  ⚠️")
        return None

def listar():
    try:
        cursor.execute("SELECT * FROM ventas")
        registros = cursor.fetchall()
        if registros:
            return registros
        else:
            print("\t\t\t⚠️  No hay ventas registradas.  ⚠️")
            return None
    except Exception as e:
        print(f"⚠️  Ocurrió un error: {e}  ⚠️")
        return None


