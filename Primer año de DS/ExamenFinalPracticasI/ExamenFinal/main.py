import modulo as m

frase = input("Ingrese una frase ")
frase_encriptada = ""
m.menu()
opcion = input("Ingrese una opcion: ")
while opcion != "6":
    if opcion == "1":
        caracter = input("Ingrese un caracter ")
        cantidad_caracteres = m.caracter(frase, caracter)
        if cantidad_caracteres == 0:
            print(f"El caracter {caracter}, no existe en la frase")
        else:
            print(f"La cantidad de {caracter} que hay en la frase, es de {cantidad_caracteres}")
    elif opcion == "2":
        caracter = input("Ingrese un caracter ")
        posicion = m.posicion(frase, caracter)
        if len(posicion) == 0:
            print(f"El caracter {caracter}, no existe en la frase")
        else:
            print(f"Las posiciones en las que se encuentra {caracter}, son: {posicion}")
    elif opcion == "3":
        frase_encriptada = m.encriptar(frase)
        if frase_encriptada == frase:
            print("La frase no se pudo encriptar")
        else:
            print(frase_encriptada)
    elif opcion == "4":
        if len(frase_encriptada) == 0:
            print(m.desencriptar(frase))
        else:
            frase_desencriptada = m.desencriptar(frase_encriptada)
            print(frase_desencriptada)
    elif opcion == "5":
        frase = input("Ingresa una nueva frase ")
    else:
        print("Opcion Erronea")
    m.menu()
    opcion = input("Ingrese una opcion ")
