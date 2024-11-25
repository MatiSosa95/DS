Alumno={"nombre": "Pablo","Edad": 30, "legajo": 32391}

#Otra manera
Alumno2=dict([
    ("nombre", "Matias"),
    ("Edad", 29),
    ("legajo", 40299)
])


# print(Alumno2["nombre"])
# print(Alumno.get("nombre"))
Alumno["nombre"]="Pablo Daniel"
Alumno["direccion"]="Calle falsa 123"
Alumno["carrera"]="Desarrollo de Software"
Alumno["Turno"]="Tarde"
Alumno["¿Trabaja?"]= True

#Eliminamos
del Alumno2["legajo"]
# print(Alumno2)

if "direccion" in Alumno:
    print("Existe")

print("---------------Clave-Valor------------------")
for clave, valor in Alumno.items():
    print(clave, valor)
print("---------------Clave------------------")
for x in Alumno:
    print(x)
print("---------------Valor------------------")
for v in Alumno:
    print(Alumno[v])

print(Alumno2)
Alumno2.clear()
print(Alumno2)

print(Alumno.get("carrera"))
lista= Alumno.items()
print(lista)
print(list(lista))

lista_claves= Alumno.keys()
print(lista_claves)
print(list(lista_claves))

lista_valores= Alumno.keys()
print(lista_valores)
print(list(lista_valores))
print("-----------------------")
#Metodo pop elimina la clave y el valor, y muestra por pantalla lo que ha borrado
Alumno["sede"]= "Maipu"
print(Alumno)
Alumno.pop("sede")
print(Alumno)

# Alumnos={}
# clave= "nombre"
# while clave.upper()!="T" and clave.upper()!="":
#     clave= input("Ingrese la clave")
#     if  clave.upper()!="T" and clave.upper()!="":
#         valor= input("Ingrese el valor")
#         Alumnos[clave]= valor
# print(Alumnos)
menu="""
Ingrese lo que desee ingresar: 
1-Alumnos
2-Carrera
3-Docente
4-Salir"""

IES={}
opcion=0
while opcion!=4:
    print(menu)
    opcion=int(input())

    if opcion==1:
        alumnos = {}
        alumnos["nombre"] = input("Ingrese el nombre del alumno ")
        alumnos["DNI"] = input("Ingrese el DNI del alumno ")
        alumnos["edad"] = int(input("Ingrese la edad del alumno "))
        alumnos["legajo"] = int(input("Ingrese el legajo del alumno "))
        alumnos["direccion"] = input("Ingrese la direccion del alumno ")
        alumnos["mail"] = input("Ingrese el mail del alumno ")
        alumnos["carrera"] = input("Ingrese la carrera del alumno ")
        alumnos["turno"] = input("Ingrese el turno en el que va al alumno")
        IES["alumnos"] = alumnos
    elif opcion==2:
        carrera = {}
        carrera["nombre"] = input("Nombre de la carrera")
        carrera["resolucion"] = input("Ingrese la resolucion")
        carrera["Turnos"] = input("ingrese los turnos que exiten")
        carrera["años"] = input("cantidad de años")
        IES["carrera"] = carrera
    elif opcion==3:
        docente = {}
        docente["nombre"] = input("Ingrese el nombre del docente ")
        docente["legajo"] = input("Legajo del docente ")
        docente["contacto"] = input("Ingrese el numero de telefono")
        docente["carrera"] = input("Ingrese la carrera")
        docente["materia"] = input("Materia que da")
        IES["docente"] = docente

print(IES)

