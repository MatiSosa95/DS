def Ejercicio1():
    personas_entrevistadas=1
    personas_chocolate=0
    merienda_completa=0
    chocolate="A"

    while chocolate != "":
        chocolate = input(f"Encuestado nro {personas_entrevistadas} ¿Le gusta el chocolate caliente? (S/N) ")
        personas_entrevistadas += 1
        if chocolate.upper() == "S":
            personas_chocolate += 1
            churro = input("Le gusta acompañado con churros? (S/N) ")
            if churro.upper() == "S":
                merienda_completa += 1
                nota= input("Del 1 al 10,¿Que nota le pondría a la merienda ?")
                if nota!="":
                    print(f"Encuestado nro {personas_entrevistadas} le puso un {nota} a la merienda")
                else:
                    print()


    print(f"Las cantidad de personas entrevistadas es de {personas_entrevistadas-1}")
    print(f"La cantidad de personas que les gusta el chocolate caliente es de {personas_chocolate}")
    print(f"La cantidad de personas que les gusta el chocolate caliente con churro es de {merienda_completa}")

def Ejercicio2():
    lista_amigos=[("Juan", 29, "Melvin"), ("Lucas", 30, "Gaseosa") , ("Franco",29, "Cerveza"),
                  ("Abel", 29, "Coca Cola"),("Fernando", 29, "Fernet") ]
    i=0
    edad=0
    edad_total=0
    mi_nombre= "Matias"
    mi_edad= 29
    mi_bebida="Agua"
    while i<=len(lista_amigos)-1:
        nombre, edad, bebida= lista_amigos[i]

        edad_total= edad+edad_total
        print(f"Este es mi amigo {nombre}, tiene {edad} años y su bebida favorita es {bebida}")
        i+=1

    edad_total+=mi_edad
    promedio= edad_total/(len(lista_amigos)+1)
    print(f"Yo soy {mi_nombre}, tengo {mi_edad} años y tomo {mi_bebida}")
    print(f"El promedio de nuestras edades es de {round(promedio,2)}")

def Ejercicio3():
    menu= """
          MENÚ
    1. Ingresa Operandos
    2.Sumar
    3.Restar
    4.Multiplicar
    5.Dividir
    6.Salir
    Elija una opcion"""
    print(menu)
    option=int(input())
    num1=None
    num2=None

    while option!=6:
        if option==1:
            num1= float(input("Ingrese el primer numero"))
            num2= float(input("Ingrese el segundo numero"))

        if option==2 and num1==None and num2==None:
            print("Regrese a la opcion 1")
        elif option==2:
            print(f"La suma de {num1} y {num2} es de: ", num1+num2)

        if option==3 and num1==None and num2==None:
            print("Regrese a la opcion 1")
        elif option==3:
            print(f"La resta de {num1} y {num2} es de: ", num1-num2)

        if option==4 and num1==None and num2==None:
            print("Regrese a la opcion 1")
        elif option==4:
            print(f"La multiplicacion de {num1} y {num2} es de: ", num1*num2)

        if option==5 and num1==None and num2==None:
            print("Regrese a la opcion 1")
        elif option==5 and num2!=0:
            print(f"La division de {num1} y {num2} es de: ", num1/num2)
        elif option==5 and num2==0:
            print("Ingresó 0 en el denominador y cualquier numero dividido por 0, da una indeterminacion")

        if option>6 or option<1:
            print("Opcion Incorrecta")
        print(menu)
        option = int(input())

def Ejercicio5():
    meses=[("Enero","Inamovible"),("Febrero","Inamovible"),("Marzo","Inamovible"), ("Abril","Inamovible"), (
        "Mayo","Inamovible"), ("Junio","Inamovible"), ("Julio","Inamovible"),("Agosto","Movible"),("Septiembre","Movible"),
                 ("Octubre","Turistico"),("Noviembre","Turistico") ,("Diciembre","Inamovible")]

    i=0
    while i<=len(meses)-1:
        mes,tipo_feriado= meses[i]
        if tipo_feriado=="Inamovible":
            print(f"El mes de {mes}, tiene feriados {tipo_feriado}")
        else:
            print(f"El mes de {mes}, tiene feriados {tipo_feriado}")
        i+=1

def Ejercicio5_2():
    meses= ("enero","febrero","marzo","abril","mayo","junio","julio","diciembre" )
    tipo_feriado =("inamovibles", "turistico" , "movibles")
    for i in range(len(meses)):
       print(f"el mes de {meses[i]} tiene feriado ", end="")
       for j in range(len(tipo_feriado)):
           if tipo_feriado[j] == "turistico" or tipo_feriado[j] == "movibles":
               continue
           print(tipo_feriado[j])


# Desarrollar un programa que calcule cuantas formas existen para lograr un total de 10 entre tres dados. Luego
    #calcule la probabilidad de tirar un diez con precisión a tres lugares
def desafio():
    cantidad_de_combinaciones= pow(6,3)
    contador= 0

    for dado1 in range(1,7):
        for dado2 in range(1,7):
            for dado3 in range(1,7):
                if dado1+dado2+dado3 == 10: 
                    #print(f"{dado1} {dado2} {dado3}") Muestro las combinaciones de dados
                    contador+=1

    print(f"La cantidad de combinacion de 3 dados que dan 10 es de {contador}")
    probabilidad= (round(contador / cantidad_de_combinaciones, 3)) * 100
    print(f"Mientras que la probabilidad es de {probabilidad}%")


meses = ["enero","febrero", "marzo","abril","mayo","junio"]
for _ in range(5):
    meses.append(input("Ingrese el mes"))
meses.insert(len(meses), "diciembre")
print(meses)