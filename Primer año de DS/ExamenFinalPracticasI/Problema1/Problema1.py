# Problema1 a resolver
# Cada mañana, el preceptor del Colegio XYZ toma la asistencia de 20 cursos. Esta tarea le toma aproximadamente una hora y media.
# Ya que tiene que esperar la respuesta del alumno y anotar manualmente cada nombre en la lista. Durante este tiempo,
# el preceptor se atrasa con sus obligaciones.
# Propone una solución tecnológica para agilizar y optimizar este proceso.
from datetime import datetime

# Listado de presentes en cada curso
# Listado de presentes de cada curso en determinada fecha.
menu = """
Ingrese el curso: 
1- Curso 1
2- Curso 2
3- Salir\n"""

menu2 = """
Ingrese la opcion: 
1- Tomar Lista
2- Ver presentes en fecha actual
3- Ver presentes en una fecha en particular
4- Salir\n"""

fecha_actual = datetime.now()
fecha_actual = str(fecha_actual.strftime("%d-%m-%Y"))
Lista_alumnos_curso1 = ["Ali", "Almeda", "Alcorta", "Bustos"]
Lista_alumnos_curso2 = ["Acevedo", "Aguilar", "Alvarado", "Arenas"]
Cursos = {
    "curso1": {"07-12-2024": {"Ali": "p", "Almeda": "p", "Alcorta": "a", "Bustos": "p"},
               "08-12-2024": {"Ali": "a", "Almeda": "p", "Alcorta": "p", "Bustos": "p"},
               "09-12-2024": {"Ali": "p", "Almeda": "p", "Alcorta": "p", "Bustos": "p"},
               "10-12-2024": {"Ali": "p", "Almeda": "p", "Alcorta": "p", "Bustos": "p"},
               "11-12-2024": {"Ali": "p", "Almeda": "a", "Alcorta": "p", "Bustos": "p"}},
    "curso2": {"07-12-2024": {"Acevedo": "p", "Aguilar": "a", "Alvarado": "a", "Arenas": "a"},
               "08-12-2024": {"Acevedo": "p", "Aguilar": "a", "Alvarado": "a", "Arenas": "a"},
               "09-12-2024": {"Acevedo": "p", "Aguilar": "a", "Alvarado": "a", "Arenas": "a"},
               "10-12-2024": {"Acevedo": "p", "Aguilar": "a", "Alvarado": "a", "Arenas": "a"},
               "11-12-2024": {"Acevedo": "p", "Aguilar": "a", "Alvarado": "a", "Arenas": "a"}}
}

flag = True
while flag:
    opcion = input(menu)
    if opcion == "1":
        flag2 = True
        while flag2:
            opcion2 = input(menu2)
            if opcion2 == "1":
                c1 = {}
                for key, value in Cursos.items():
                    if key == "curso1":
                        for i in Lista_alumnos_curso1:
                            flag3 = True
                            while flag3:
                                print(i)
                                presentismo = input("Ingrese p para presente o a, para ausente")
                                if presentismo != "p" and presentismo != "a":
                                    print("Opcion Erronea")
                                else:
                                    c1[i] = presentismo
                                    flag3 = False
                Cursos["curso1"][fecha_actual] = c1

            if opcion2 == "2":
                if Cursos["curso1"].get(fecha_actual) is None:
                    print("Debe tomar presente primero")
                else:
                    for key, value in Cursos.items():
                        if key == "curso1":
                            for key1, value1 in Cursos["curso1"][fecha_actual].items():
                                if value1 == "p":
                                    print(key1)
            if opcion2 == "3":
                flag3 = True
                while flag3:
                    fecha = input("Ingrese una fecha valida: dd-mm-yyyy: ")
                    if Cursos["curso1"].get(fecha) is None:
                        print("No existe la fecha deseada")
                        flag3 = False
                    else:
                        for key, value in Cursos.items():
                            if key == "curso1":
                                for key1, value1 in Cursos["curso1"][fecha].items():
                                    if value1 == "p":
                                        print(key1)
                                flag3 = False
            if opcion2 == "4":
                flag2 = False
    if opcion == "2":
        flag2 = True
        while flag2:
            opcion2 = input(menu2)
            if opcion2 == "1":
                c1 = {}
                for key, value in Cursos.items():
                    if key == "curso2":
                        for i in Lista_alumnos_curso2:
                            flag3 = True
                            while flag3:
                                print(i)
                                presentismo = input("Ingrese p para presente o a, para ausente")
                                if presentismo != "p" and presentismo != "a":
                                    print("Opcion Erronea")
                                else:
                                    c1[i] = presentismo
                                    flag3 = False
                Cursos["curso2"][fecha_actual] = c1

            if opcion2 == "2":
                if Cursos["curso2"].get(fecha_actual) is None:
                    print("Debe tomar presente primero")
                else:
                    for key, value in Cursos.items():
                        if key == "curso2":
                            for key1, value1 in Cursos["curso2"][fecha_actual].items():
                                if value1 == "p":
                                    print(key1)
            if opcion2 == "3":
                flag3 = True
                while flag3:
                    fecha = input("Ingrese una fecha valida: dd-mm-yyyy: ")
                    if Cursos["curso2"].get(fecha) is None:
                        print("No existe la fecha deseada")
                        flag3 = False
                    else:
                        for key, value in Cursos.items():
                            if key == "curso2":
                                for key1, value1 in Cursos["curso2"][fecha].items():
                                    if value1 == "p":
                                        print(key1)
                                flag3 = False
            if opcion2 == "4":
                flag2 = False
    if opcion == "3":
        flag = False
