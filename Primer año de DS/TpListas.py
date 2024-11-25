# def ejercicio1_2_3_4_5_6():
#     # Ejercicio 1
#     amigos = []
#     cant_amigos = int(input("¿Cuantos amigos tiene?"))
#     for i in range(cant_amigos):
#         mellow = input("¿Cual es su amigo numero {}? ".format(i + 1))
#         amigos.append(mellow)
#
#     print(amigos)
#
#     # Ejercicio 2
#     edades = []
#     for i in range(cant_amigos):
#         edad = input("¿Cual es la edad de su amigo {}? ".format(amigos[i]))
#         edades.append(edad)
#
#     print(edades)
#     # Ejercicio 3
#     amigo_curso= input("Ingrese el nombre de un compañero")
#     amigos.append(amigo_curso)
#
#     # Ejercicio 4
#     amigo_trabajo1 = "Federico"
#     amigo_trabajo2 = "Gustavo"
#     amigo_trabajo3 = "Miguel"
#
#     amigos.insert(0, amigo_trabajo1)
#     amigos.insert((len(amigos) // 2) + 1, amigo_trabajo2)
#     amigos.insert(len(amigos), amigo_trabajo3)
#
#     print(amigos)
#
#     # Ejercicio 5
#     amigo_viejo= input("Ingrese el nombre de su amigo mas anciano")
#     if amigo_viejo in amigos:
#         indice= amigos.index(amigo_viejo)
#         amigos[indice]= "Rectora del IES"
#
#     print(amigos)
#
#     #Ejercicio 6
#     borrar = input("Ingrese el nombre de su amigo que desee borrar")
#
#     for i in amigos:
#         if borrar == i:
#             amigos.remove(i)
#
#     print(amigos)
#
#
# def ejercicio7():
#     lista_vacia=[]
#
#     while True:
#         nombre= input("Ingrese el nombre de la persona que vio hoy ")
#         if nombre=="":
#             break
#         lista_vacia.append(nombre)
#
#
#     print(lista_vacia)


# DESAFIO
#Entrada: Lista Vacio
#Proceso: Se ingresan numeros a la lista vacia, la cual se van comparando con el while, para sacar el numero mas grande ingresado
#Salida: Muestra la lista ya creada, el tamaño de la misma, el valor mas pequeño y el mas grande.
valores = []
entrada = input ("Ingrese un número o enter para terminar")
if entrada =="" :
    print ("Debe intoducir un numero")
    entrada = input ("Ingrese un número o enter para terminar")

while entrada !="":
    valores.append (float(entrada))
    entrada = input("Ingrese un número o Enter para terminar: ")

desorden = True
while desorden:
    desorden = False
    for i in range (len(valores)-1):
        if valores[i+1] < valores[i]:
            desorden = True
            valor = valores [i+1]
            valores [i+1] = valores [i]
            valores [i] = valor

print ("El listado inicial es: ", valores)
tamaño = len(valores)
print ("El tamaño de la lista es: ", tamaño)
print ("El elemento mas pequeño es: ", valores[0])
print ("El elemento mas grande es: ", valores[tamaño-1])