from conexion import Conexion

class Venta:

    @staticmethod
    def check_id_cliente(id_cliente):
        try:
            Conexion.cursor.execute(
                "select * from clientes where id=%s",(id_cliente,)
            )
            registro=Conexion.cursor.fetchone()
            return True if registro else None
        except:
            return None

    @staticmethod
    def check_id_usuario(id_usuario):
        # Esta función realmente verifica el usuario, debería estar en la clase Usuario
        # Pero la mantengo aquí por la lógica original.
        try:
            Conexion.cursor.execute(
                "select * from usuarios where id=%s",(id_usuario,)
            )
            registro=Conexion.cursor.fetchone()
            return True if registro else None
        except:
            return None

    @staticmethod
    def check_id_venta(id_venta):
        try:
            Conexion.cursor.execute(
                "select * from ventas where id=%s",(id_venta,)
            )
            registro=Conexion.cursor.fetchone()
            return True if registro else None
        except:
            return None

    @staticmethod
    def imprimir_tabla_ventas(registros):
        print(f"+{'-'*5}+{'-'*12}+{'-'*13}+{'-'*10}+{'-'*15}+{'-'*20}+{'-'*12}+")
        print(f"| {'ID':<3} | {'ID Usuario':<10} | {'ID Cliente':<11} | {'Monto':<8} | {'# Prendas':<13} | {'Método de Pago':<18} | {'Fecha':<10} |")
        print(f"+{'-'*5}+{'-'*12}+{'-'*13}+{'-'*10}+{'-'*15}+{'-'*20}+{'-'*12}+")
        for venta_reg in registros:
            print(f"| {venta_reg[0]:<3} | {venta_reg[1]:<10} | {venta_reg[2]:<11} | {venta_reg[3]:<8.2f} | {venta_reg[4]:<13} | {venta_reg[5]:<18} | {str(venta_reg[6]):<10} |")
            print(f"+{'-'*5}+{'-'*12}+{'-'*13}+{'-'*10}+{'-'*15}+{'-'*20}+{'-'*12}+")

    @staticmethod
    def crear(usuario_id, id_cliente, monto, nprendas, metodopago):
        try:
            Conexion.cursor.execute(
                "insert into ventas (id_usuario, id_cliente, monto, num_prendas, metodo_pago, fecha) values (%s,%s,%s,%s,%s,NOW())",
                (usuario_id, id_cliente, monto, nprendas, metodopago)
            )
            Conexion.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear venta: {e}")
            return None
        

    @staticmethod
    def consultar(id_venta):
        try:
            Conexion.cursor.execute("select * from ventas where id=%s", (id_venta,))
            registro = Conexion.cursor.fetchone()
            return registro
        except:
            return None
        

    @staticmethod
    def actualizar(usuario_id):
        try:
            Conexion.cursor.execute("SELECT * FROM ventas")
            registros = Conexion.cursor.fetchall()
            if not registros:
                print("\t\t\t⚠️  No hay ventas registradas.  ⚠️")
                return None

            Venta.imprimir_tabla_ventas(registros)
            op = input("¿Desea actualizar algúna venta? (S/N): ").strip().upper()
            if op != 'S':
                print("⚠️  Operacion cancelada  ⚠️")
                return None
            
            id_venta = input("Ingrese el ID de la venta a actualizar: ").strip()
            if not Venta.check_id_venta(id_venta):
                print("❌ La venta no existe.")
                return None
            
            id_cliente = input("Ingrese el ID de cliente: ").strip()
            if not Venta.check_id_cliente(id_cliente):
                print("❌ El cliente no existe.")
                return None
            
            while True:
                monto = input("Monto: ")
                try:
                    monto = float(monto)
                    break
                except ValueError:
                    print("\t⚠️  Solo valores numéricos  ⚠️")
            
            while True:
                nprendas = input("Ingrese el nuevo número de prendas: ").strip()
                if nprendas.isdigit():
                    break
                else:
                    print("⚠️  Solo valores numericos  ⚠️")
            
            while True:
                metodopago = input("Ingrese el nuevo método de pago (Efectivo=E/Transfrenecia=T): ").strip().lower()
                if metodopago == "e":
                    metodopago = "EFECTIVO"
                    break
                elif metodopago == "t":
                    metodopago = "TRANSFERENCIA"
                    break
                else:
                    print("\t⚠️  Solo Efectivo=E/Transfrenecia=T  ⚠️")
            
            Conexion.cursor.execute("UPDATE ventas SET id_usuario=%s, id_cliente=%s, monto=%s, num_prendas=%s, metodo_pago=%s WHERE id=%s",
                                    (usuario_id, id_cliente, monto, nprendas, metodopago, id_venta))
            Conexion.conexion.commit()
            return id_venta
        except Exception as e:
            print(f"⚠️  Ocurrió un error: {e}  ⚠️")
            return None

    @staticmethod
    def borrar():
        try:
            Conexion.cursor.execute("SELECT * FROM ventas")
            registros = Conexion.cursor.fetchall()
            if not registros:
                print("\t\t\t⚠️  No hay ventas registradas.  ⚠️")
                return None
            
            Venta.imprimir_tabla_ventas(registros)
            
            print("\n\t\t..::: Eliminar Ventas :::...")
            op = input("¿Desea eliminar algúna venta? (S/N): ").strip().upper()
            if op == 'S':
                id_venta = input("Ingrese el ID de la venta a eliminar: ").strip()
                existe = Venta.check_id_venta(id_venta)
                if not existe:
                    print("⚠️  La venta no existe.  ⚠️")
                    return None
                
                opcion = input(f"¿Seguro que desea eliminar la venta {id_venta}? (S/N): ").strip().upper()
                if opcion == 'S':
                    Conexion.cursor.execute("DELETE FROM ventas WHERE id = %s", (id_venta,))
                    Conexion.conexion.commit()
                    return id_venta
                else:
                    print("⚠️  Operación cancelada.  ⚠️")
                    return None
            else:
                print("⚠️  Operación cancelada.  ⚠️")
                return None
        except Exception as e:
            print(f"⚠️  Ocurrió un error: {e}  ⚠️")
            return None

    @staticmethod
    def listar():
        try:
            Conexion.cursor.execute("SELECT * FROM ventas")
            registros = Conexion.cursor.fetchall()
            if registros:
                return registros
            else:
                print("\t\t\t⚠️  No hay ventas registradas.  ⚠️")
                return None
        except Exception as e:
            print(f"⚠️  Ocurrió un error: {e}  ⚠️")
            return None