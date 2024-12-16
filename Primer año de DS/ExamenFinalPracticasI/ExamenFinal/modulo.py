def menu():
    menu = """
    Menu
    1- Cantidad de un caracter
    2- Posicion de un caracter
    3- Encriptar
    4- Descriptar
    5- Ingresar una nueva frase
    6- Salir"""

    print(menu)


def caracter(frase, caracter):
    contador = 0
    for i in frase:
        if caracter.lower() == i.lower():
            contador += 1
    return contador


def posicion(frase, caracter):
    posiciones = []

    for i in range(len(frase)):
        if frase[i].lower() == caracter.lower():
            posiciones.append(i+1)
    return posiciones


def encriptar(frase):
    frase_encriptada = (frase.lower().replace("a", "@").
                        replace("e", "3").
                        replace("i", "!").
                        replace("o", "0").
                        replace("u", "#"))

    return frase_encriptada


def desencriptar(frase_encriptada):
    frase = (frase_encriptada.lower().replace("@", "a").
             replace("3", "e").
             replace("!", "i").
             replace("0", "o").
             replace("#", "u").capitalize())
    return frase
