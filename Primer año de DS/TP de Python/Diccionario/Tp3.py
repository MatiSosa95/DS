import random as r

def Ejercicio1(magnitud):
    if magnitud<4:
        print(f"Con magnitud de {magnitud}, no hay daños")
    elif magnitud<=5.9:
        print(f"Con magnitud de {magnitud}, daños en edificios mal construidos")
    elif magnitud <= 6.9:
        print(f"Con magnitud de {magnitud}, muchos edificios dañados, algunos colapsados")
    elif magnitud <= 7.9:
        print(f"Con magnitud de {magnitud}, muchos edificios destruidos")
    else:
        print(f"Con magnitud de {magnitud}, la mayoria de los edificios caen")

def Ejercicio2(cant_total, cant_correctas):
    datos= int((cant_correctas/cant_total)*100)
    print(datos)
    if datos<50:
        print("Fuera de Nivel")
    elif datos<70:
        print("Nivel Regular")
    elif datos<90:
        print("Nivel Medio")
    else:
        print("Nivel maximo")

def Ejercicio3():

    menu= """
        Elija su opcion con numeros
        1. Su hijo tiene menos de un año
        2. Su hijo tiene mas de un año"""
    print(menu)
    seleccion= int(input())

    match seleccion:
        case 1:
            edad= int(input("Ingrese la edad de su hijo en meses "))
            hemoglobina= float(input("Ingrese el porcentaje de hemoglobina en sangre "))

            if edad<=1 and (hemoglobina>=13 and hemoglobina<=26):
                print("No tiene anemia")
            elif (edad>1 and edad<=6) and (hemoglobina>=10 and hemoglobina<=18):
                print("No tiene anemia")
            elif (edad>6 and edad<=12) and (hemoglobina>=11 and hemoglobina<=15):
                print("No tiene anemia")
            else:
                print("Tiene anemia")

        case 2:
            edad = int(input("Ingrese la edad de su hijo en años "))
            hemoglobina = float(input("Ingrese el porcentaje de hemoglobina en sangre "))
            if (edad>1 and edad<=5) and (hemoglobina >= 11.5 and hemoglobina <= 15):
                print("No tiene anemia")
            elif (edad>5 and edad<=10) and (hemoglobina >= 12.6 and hemoglobina <= 15.5):
                print("No tiene anemia")
            elif (edad>10 and edad<=15) and (hemoglobina >= 13 and hemoglobina <= 15.5):
                print("No tiene anemia")
            else:
                print("Tiene anemia")



def Ejercicio4(distancia, dias):
    distancia= distancia*2
    precio= distancia*100
    if distancia > 800 and dias > 7:
        precio= precio-precio*0.3

    print(f"El precio total que debe pagar es de {precio}")

def desafio():
    print("Primer Corredor")
    horas_A= int(input("Ingrese la hora al pasar la meta el corredor A "))
    minutos_A=int(input("Ingrese los minutos al pasar la meta el corredor A "))
    segundos_A = int(input("Ingrese los segundos al pasar la meta el corredor A "))
    tiempo_A=(horas_A, minutos_A, segundos_A)
    print("Segundo Corredor")
    horas_B = int(input("Ingrese la hora al pasar la meta el corredor B "))
    minutos_B = int(input("Ingrese los minutos al pasar la meta el corredor B "))
    segundos_B = int(input("Ingrese los segundos al pasar la meta el corredor B "))
    tiempo_B = (horas_B, minutos_B, segundos_B)
    if tiempo_A<tiempo_B:
        print("El competidor que lo hizo en menos tiempo fue el A")
    elif tiempo_B<tiempo_A:
        print("El competidor que lo hizo en menos tiempo fue el B")
    else:
        print("Ambos competidores empataron")

# Ejercicio1(round(r.uniform(0,10),2))
# Ejercicio2(10, 1.5)
# Ejercicio3()
#Ejercicio4(100, 8)
#desafio()
