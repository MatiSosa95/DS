def menu():
    menu = """
    Menú
    1-Crear lista de numeros enteros
    2-Valor segun posicion
    3-Posiciones de un valor 
    4-Lista ordenada
    5-Salir"""
    print(menu)


def crear_lista():
    vector = []
    nro = 1
    while nro != 0:
        nro = int(input("Ingrese numeros positivos a su vectors.\n Para finalizar la carga coloque 0 "))
        if nro != 0:
            vector.append(nro)
    return vector


def valor_segun_posicion(vector):
    if len(vector) == 0:
        print("Debe ingresar valores a la lista primero")
    else:
        posicion = 0
        while posicion <= 0:
            posicion = int(input(
                f"ingrese la posicion de que desea explorar.\n Recuerde las posiciones son desde 1 al {len(vector)} "))
        print(f"El valor que se encuentra en la posicion {posicion}, es {vector[posicion - 1]}")


def posiciones_valor(vector):
    if len(vector) == 0:
        print("Debe ingresar valores a la lista primero")
    else:
        valor = 0
        resultado = []
        while valor <= 0:
            valor = int(
                input(f"ingrese el valor de que desea buscar.\n Recuerde las posiciones son desde 1 al {len(vector)} "))
        for i in range(len(vector)):
            if vector[i] == valor:
                resultado.append(i + 1)
        print(f"El valor buscado se encuenta en la posicion o posiciones {resultado}")


def ordenar_lista(lista):
    if len(lista) == 0:
        print("Debe ingresar valores a la lista primero")
    else:
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] < lista[j + 1]:
                    lista[j] = lista[j + 1]
                    lista[j + 1] = lista[j]
        print(lista)
