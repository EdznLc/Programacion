'''
Es un tipo de dato que se utiliza para almacenar datos de diferente tipo de datos en
lugar de tener como las listas indices numericos tiene alfanumericos.
Es decir es algo parecido como los Objetos.

Tambien se conoce como arreglo asosiativo y Objecto JSON.

El diccionario es una coleccion ordenada y modificable. No hay miembros duplicados.
'''

import os
os.system("cls")

pais_mx={
        "Nombre":"Mexico",
        "Capital":"CDMEX",
        "Poblacion":"12000000",
        "Idioma":"Espagnol",
        "Status":True
        }

pais_br={
        "Nombre":"Brasil",
        "Capital":"Brasilia",
        "Poblacion":"1000000",
        "Idioma":"Portugues",
        "Status":True
        }

pais_cnd={
        "Nombre":"Canada",
        "Capital":"Ottawa",
        "Poblacion":"90000000",
        "Idioma":["ingles","frances"],
        "Status":False
        }

alumno1={
        "Nombre":"Daniel",
        "Apellido_p":"Hernandez",
        "Apellido_m":"Gonzalez",
        "Carrera":"TI",
        "Area":"Software Multiplataforma",
        "Modalidad":"BIS",
        "Matricula":"123456",
        "Semestre":"2"
}
#Mostrar el contenido
print(alumno1)

for i in alumno1:
        print(f"{i} = {alumno1[i]}")

#Agregar
alumno1["telefono"]="6181234567"
for i in alumno1:
        print(f"{i} = {alumno1[i]}")