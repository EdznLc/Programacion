from conexionBD import *
from funciones import *

def crear(usuario_id,titulo,desc):
    try:
        cursor.execute("INSERT INTO notas(usuario_id, titulo, descripcion, fecha) values (%s, %s, %s, NOW())",(usuario_id, titulo, desc))
        conexion.commit()
        return True
    except:
        return False

def mostrar(usuario_id):
    cursor.execute("Select * from notas where usuario_id = %s",(usuario_id,))
    lista_nota=cursor.fetchall()
    return lista_nota

def cambiar(usuario_id):
    try:
        # Mostrar todas las notas del usuario
        cursor.execute("SELECT * FROM notas WHERE usuario_id = %s", (usuario_id,))
        notas = cursor.fetchall()
        if notas:
            print(f"{'-'*70}")
            print(f"{'ID':<10} {'Titulo':<15} {'Descripcion':<25} {'Fecha':<10}")
            print(f"{'-'*70}")
            for nota in notas:
                print(f"{nota[0]:<10}{nota[2]:<15} {nota[3]:<25} {nota[4]}")
                print(f"{'-'*70}")
            op = input("¿Quieres modificar una nota? (S/N): ").lower().strip()
            if op == "s":
                id_nota = input("ID de la nota a modificar: ").strip()
                # Verificar que esa nota pertenezca al usuario
                cursor.execute("SELECT * FROM notas WHERE id = %s AND usuario_id = %s", (id_nota, usuario_id))
                nota = cursor.fetchone()
                if nota:
                    borrarPantalla()
                    print(f"{'-'*70}")
                    print(f"{'ID':<10} {'Titulo':<15} {'Descripcion':<25} {'Fecha':<10}")
                    print(f"{'-'*70}")
                    print(f"{nota[0]:<10}{nota[2]:<15} {nota[3]:<25} {nota[4]}")
                    print(f"{'-'*70}")
                    # Pedir nuevos datos
                    titulo = input("Nuevo título: ")
                    descripcion = input("Nueva descripción: ")
                    cursor.execute("UPDATE notas SET titulo = %s, descripcion = %s, fecha = NOW() WHERE id = %s",(titulo, descripcion, id_nota))
                    conexion.commit()
                    return True
                else:
                    print("⚠️ La nota no existe o no pertenece al usuario.")
                    return False
            else:
                return False
        else:
            print("⚠️ No hay notas registradas para este usuario.")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def borrar(usuario_id):
    try:
        # Mostrar todas las notas del usuario
        cursor.execute("SELECT * FROM notas WHERE usuario_id = %s", (usuario_id,))
        notas = cursor.fetchall()
        if notas:
            print(f"{'-'*70}")
            print(f"{'ID':<10} {'Título':<15} {'Descripción':<25} {'Fecha':<10}")
            print(f"{'-'*70}")
            for nota in notas:
                print(f"{nota[0]:<10}{nota[2]:<15} {nota[3]:<25} {nota[4]}")
                print(f"{'-'*70}")
            op = input("¿Quieres eliminar una nota? (S/N): ").lower().strip()
            if op == "s":
                id_nota = input("ID de la nota a eliminar: ").strip()
                # Verificar que esa nota pertenece al usuario
                cursor.execute("SELECT * FROM notas WHERE id = %s AND usuario_id = %s", (id_nota, usuario_id))
                nota = cursor.fetchone()
                if nota:
                    borrarPantalla()
                    print(f"{'-'*70}")
                    print(f"{'ID':<10} {'Título':<15} {'Descripción':<25} {'Fecha':<10}")
                    print(f"{'-'*70}")
                    print(f"{nota[0]:<10}{nota[2]:<15} {nota[3]:<25} {nota[4]}")
                    print(f"{'-'*70}")
                    confirmar = input("¿Estás completamente seguro de eliminar esta nota? (S/N): ").lower().strip()
                    if confirmar == "s":
                        cursor.execute("DELETE FROM notas WHERE id = %s", (id_nota,))
                        conexion.commit()
                        print("✅ Nota eliminada exitosamente.")
                        return True
                    else:
                        print("❌ Eliminación cancelada.")
                        return False
                else:
                    print("⚠️ La nota no existe o no pertenece al usuario.")
                    return False
            else:
                return False
        else:
            print("⚠️ No hay notas registradas para este usuario.")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False