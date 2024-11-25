import json
lenguajes_programacion= {
    "Nombres": ["Fortran", "COBOL", "C", "Java", "Python"],
    "Anio de creacion": [1957,1959,1972, 1995, 1991],
    "Creador": ["John Backus", "Grace Hopper", "Dennis Ritchie", "James Gosling", "Guido van Rossum"],
    "Descripcion": ["Uno de los primeros lenguajes de programacion de alto nivel",
                    "Lenguaje de programación diseñado para aplicaciones empresariales, enfocado en procesamiento de datos y transacciones",
                    "Un lenguaje de programacion de proposito general, conocido por su eficiencia y control sobre hardware",
                    "Un lenguaje diseñado para ser portatil, con un enfoque en la independencia de la plataforma, ampliamente utilizado en aplicaciones empresariales y moviles",
                    "Un lenguaje de proposito general con una sintaxis sencilla y clara, conocido por su facilidad de uso y versatilidad."]
}

def alta(diccionario):
    nombre= input("Ingrese el nomnbre del lenguaje de programacion que desee ingresar")
    anio_creacion= int(input(f"Ingrese el año de creacion de {nombre}"))
    creador= input(f"Ingrese el nombre del creador de {nombre}")
    descripcion= input(f"Coloque una corta descripcion del lenguaje {nombre}")

    diccionario["Nombres"][len(diccionario)]= nombre
    diccionario["Anio de creacion"][len(diccionario)] = anio_creacion
    diccionario["Creador"][len(diccionario)] = creador
    diccionario["Descripcion"][len(diccionario)] = descripcion

def baja(diccionario):
    eliminar= input("¿Qué lenguaje desea eliminar?")
    for elemento in diccionario["Nombres"]:
        if elemento.lower() == eliminar.lower():
            indice = diccionario["Nombres"].index(elemento)
            del diccionario["Nombres"][indice]
            del diccionario["Anio de creacion"][indice]
            del diccionario["Creador"][indice]
            del diccionario["Descripcion"][indice]





# alta(lenguajes_programacion)
# lenguajes_programacion= json.dumps(lenguajes_programacion, sort_keys=False, indent=3)
# print(lenguajes_programacion)
baja(lenguajes_programacion)

lenguajes_programacion= json.dumps(lenguajes_programacion, sort_keys=False, indent=3)
print(lenguajes_programacion)


