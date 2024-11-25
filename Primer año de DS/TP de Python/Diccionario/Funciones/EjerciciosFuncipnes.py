# def calcula_media(*args):
#     total = 0
#     for i in args:
#         total += i
#     resultado = total / len(args)
#     return resultado
# media = calcula_media(12,8,9,6,5,8,2)
# print(f"La media {media}")
#
# def calcula_suma_media(*args):
#     total = 0
#     for i in args:
#         total +=i
#     media = total / len(args)
#     return total,media
# nro1 = int(input("Ingrese el primer nro:"))
# nro2 = int(input("Ingrese el segundo nro:"))
# nro3 = int(input("Ingrese el tercer nro:"))
# total, media = calcula_suma_media(nro1, nro2, nro3)
# print(f"Datos: {nro1, nro2, nro3}")
# print(f"La suma de los argumentos es de : {total}")
# print(f"La media de los argumentos es de: {media}")
#
# def aplicar_funcion_a_cada_elemento(lista, funcion):
#     resultados = []
#     for elemento in lista:
#         resultado = funcion(elemento)
#         resultados.append(resultado)
#     return resultados
# def elevar_al_cuadrado(x):
#     return x**2
#
# listadenros = [1, 2, 3, 4]
# cuadrados = aplicar_funcion_a_cada_elemento(listadenros, elevar_al_cuadrado)
# print(cuadrados)

# def agregar_elemento(lista):
#  lista.append(5)
#
# mi_lista = [1, 2, 3,4]
# agregar_elemento(mi_lista)
# print(mi_lista) # Imprime [1, 2, 3, 4, 5]


