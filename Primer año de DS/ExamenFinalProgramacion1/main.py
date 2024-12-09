import funciones as f

f.menu()
opcion = input("Ingrese una opcion ")
lista_numero = []
while opcion != "5":
    if opcion == "1":
        lista_numero = f.crear_lista()
        print(lista_numero)
    elif opcion == "2":
        f.valor_segun_posicion(lista_numero)
    elif opcion == "3":
        f.posiciones_valor(lista_numero)
    elif opcion == "4":
        f.ordenar_lista(lista_numero)
    else:
        print("Opcion Erronea")
    f.menu()
    opcion = input("Ingrese una opcion ")
