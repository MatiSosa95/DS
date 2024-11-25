def problema1():
    for i in range(1, 11):
        print(f"El valor de {i} y su cuadrado es {i*i}")

def problema1_lista():
    lista= [1,2,3,4,5,6,7,8,9,10]
    for elemento in lista:
        print(f"El valor de {elemento} y su cuadrado es {elemento * elemento}")

# lenguajes= ["Python","C", "Java", "Javascript", "Kotlin"]
# contador=1
# for elemento in lenguajes:
#     print(f"El {contador}° que aprendi es {elemento}")
#     contador += 1

def problema2():
    meses = ["julio", "agosto", "setiembre", "octubre", "noviembre", "diciembre"]
    suma = 0
    for elementos in meses:
        precio = float(input(f"Ingrese lo que gasto en {elementos} "))
        suma += precio

    print(suma)
    print("El promedio del sementes es: ", round(suma / len(meses), 2))


def problema3():
    contador= 1
    lista_lugares= ["Mendoza", "San Luis", "Cordoba", "Buenos Aires", "Entre Rios", "Corrientes", "Misiones",
                    "Neuquen", "Chubut", "Santa Cruz", "Rio Negro"]

    for elementos in lista_lugares:

        print(f"El {contador}° lugar que conoci es {elementos}")
        contador+=1

def problema4():
    cantidad_numeros= int(input("Ingrese la cantidad de numeros que quiere ingresar "))
    numeros = int(input("Ingrese un numero entero "))
    nro_menor= numeros
    for _ in range(cantidad_numeros-1):
        numeros = int(input("Ingrese un numero entero "))
        if numeros<nro_menor:
            nro_menor=numeros

    print("El numero mas chico que ingresó es ", nro_menor)

def problema5():
    frase= input("Ingrese una frase ")
    posicion=1
    vocales=0
    mayusculas=0

    for i in frase:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            print(f"En la posicion {posicion} se encontró la vocal {i}")
            vocales+=1
            posicion+=1

        if i.isupper():
            print(f"En la posicion {posicion} se encontró la mayuscula {i}")
            mayusculas += 1
            posicion += 1

    print(f"La cantidad de mayusculas es de {mayusculas} y de vocales {vocales}")

def problema6():
    cant_asteriscos= int( input("Ingrese la cantidad de asteriscos "))
    for i in range(1, cant_asteriscos+1):
        for j in range(i):
            print("*", end= '')
        print()

def problema7():
    cantidad_numeros = int(input("Ingrese la cantidad de numeros que quiere ingresar "))
    numeros = int(input("Ingrese un numero entero "))
    nro_mayor = numeros
    i=1
    while i< cantidad_numeros:
        numeros = int(input("Ingrese un numero entero "))
        if numeros > nro_mayor:
            nro_mayor = numeros
        i+=1

    print("El numero mas grande que ingresó es ", nro_mayor)

def problema8():
    meses=[("Julio", 31),("Agosto", 31),("Septiembre", 30),("Octubre", 31), ("Noviembre", 30),("Diciembre", 31)]
    i=0
    while i<len(meses):
        mes, dia= meses[i]

        if dia==31:
            print(f"Los meses con 31 dias en el ultimo semestre son {mes}")
        i+=1

