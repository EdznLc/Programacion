peliculas=[]

def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    print("Oprima cualquier tecla para continuar ...")
    input()  

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Peliculas ::. ")
    peliculas.append(input("Ingresa el nombre: ").upper().strip())
    input("\n\t:::. La operacion se realizo con exito .:::")

def consultarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o Mostrar las Peliculas ::.")
    if len(peliculas)>0:
        for i in range(0,len(peliculas)):
            print(f"{i+1}: {peliculas[i]}")
    else:
        print("\t::. No hay peliculas en el sistema .::")

def vaciarPeliculas():
    borrarPantalla()
    print("\n\t::.Borrar o quitar todas las peliculas.::")
    resp=input("Deseas quitar/borrar todas las peliculas del sistema? s/n ").lower()
    if resp=="s":
        peliculas.clear()
        input("\n\t:::. La operacion se realizo con exito .:::")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t::.Buscar Pliculas.::")
    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print("No se encuentra la pelicula a buscar")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"::.La pelicula {pelicula_buscar} esta en existencia en la casilla: {i+1}.::")
                encontro+=1
        if encontro>0:
            print(f"Tenemos {encontro} pelicula(s) con ese titulo")
            input("\n\t:::. La operacion se realizo con exito .:::")

def eliminarPeliculas():
    borrarPantalla()
    print("\n\t::.Borrar Película.::")
    pelicula_borrar = input("Ingrese el nombre de la película que desea buscar: ").upper().strip()
    borro = 0
    encontrada = False
    
    i = 0
    while i < len(peliculas):
        if peliculas[i] == pelicula_borrar:
            encontrada = True
            print(f"\nSe encontró la película en la posición {i + 1}: {peliculas[i]}")
            op = input("¿Deseas borrar esta película del sistema? (Si/No): ").lower()
            if op == "si":
                peliculas.pop(i)
                print(f"Se borró la película '{pelicula_borrar}' en la posición {i + 1}")
                borro += 1
                continue
        i += 1
    if not encontrada:
        print("No se encontró la película.")
    else:
        print("\n\t:::. La operación se realizó con éxito .:::")
        print(f"Se borró {borro} película(s) con ese título.")



def modificarPeliculas():
    borrarPantalla()
    print("\n\t::.Modificar Película.::")
    criterio = input("¿Deseas buscar por nombre o índice? (nombre/indice): ").lower().strip()

    modificadas = 0

    if criterio == "nombre":
        nombre_buscar = input("Ingrese el nombre de la película: ").upper().strip()
        encontrada = False
        for i in range(len(peliculas)):
            if peliculas[i] == nombre_buscar:
                encontrada = True
                print(f"\nSe encontró en la posición {i + 1}: {peliculas[i]}")
                op = input("¿Deseas modificar esta película? (Si/No): ").lower()
                if op == "si":
                    nuevo_nombre = input("Ingresa el nuevo nombre: ").strip().upper()
                    peliculas[i] = nuevo_nombre
                    print(f"Modificada en posición {i + 1}")
                    modificadas += 1
        if not encontrada:
            print("No se encontró ninguna película con ese nombre.")

    elif criterio == "indice":
        index_input = input("Ingresa el índice (posición) de la película: ").strip()
        if index_input.isdigit():
            index = int(index_input) - 1
            if 0 <= index < len(peliculas):
                print(f"Película actual en la posición {index + 1}: {peliculas[index]}")
                op = input("¿Deseas modificar esta película? (Si/No): ").lower()
                if op == "si":
                    nuevo_nombre = input("Ingresa el nuevo nombre: ").strip().upper()
                    peliculas[index] = nuevo_nombre
                    print("Película modificada correctamente.")
                    modificadas += 1
                else:
                    print("No se realizó ninguna modificación.")
            else:
                print("Índice fuera de rango.")
        else:
            print("Índice inválido. Debe ser un número entero positivo.")

    else:
        print("Opción inválida. Debes elegir 'nombre' o 'indice'.")

    print(f"\nSe modificó(n) {modificadas} película(s).")
