#Idea crear un programa donde los alumnos coloquen su nombre y curso.
#Tmb que coloquen que van a comprar y como lo van a pagar. En caso de ser por MP, se debe pagar antes de ir a buscarlo
#El alumno tiene hasta hasta 10 minutos antes del receso para ahcer su pedido, modificarlo, eliminarlo o pagarlo.
import time

compra = {'40299': ('Matias', '4b', 'mp', ['5 tortitas', "Papas Lays", "2 alfajores tatin"])}


def menu():
    menu = ("""
    Menu del Kiosko
    1- Comprar
    2- Modificar compra
    3- Eliminar Compra
    4- Ver compras(Administrador)
    5- salir""")
    opcion = input(menu)
    listado_productos = {
        "tortitas": 50,
        "alfajor Tatin": 100,
        "alfajor Fulbito": 75,
        "chupetin": 100,
        "Papas Lays": 250,
        "Caramelos masticables": 20,
        "Chicles": 250,
        "Chizitos": 100}
    while opcion != "5":

        if opcion == "1":
            print("Listas de Productos")
            for key, value in listado_productos.items():
                print(f"-{key} tiene un valor de ${value}")
            compra_alumnos()
        if opcion == "2":
            modificar_compra(compra)
        if opcion == "3":
            eliminar_compra()
        if opcion == "4":
            ver_compras()
        if opcion == "5":
            print("Saliendo...")
        opcion = input(menu)


def compra_alumnos():
    compra_por_alumno = []
    flag = True
    nombre = input("Ingrese su nombre ")
    legajo = input("Ingrese su legajo ")
    curso = input("Ingrese su curso ")
    medio_pago = input("Ingrese su medio de pago. Efectivo o Mercado pago (E/MP) ")

    while flag:
        productos = input("Ingrese los productos que desea comprar. Para terminar, presione 0 ")
        if productos != "0":
            compra_por_alumno.append(productos)
        else:
            flag = False

    compra[legajo] = (nombre, curso, medio_pago, compra_por_alumno)
    print(f"Compra realizada")
    return compra


def modificar_compra(diccionario):
    legajo = input("Ingrese su legajo ")
    if len(diccionario) == 0:
        print("problemas")
    for key, value in diccionario.items():
        if legajo == key:
            print(value[3])
            cambio = input("Ingrese lo que quiere cambiar")
            for i in value[3]:
                if cambio == i:
                    value[3].remove(i)
                    cambio2 = input("Ingrese el cambio")
                    value[3].append(cambio2)
        print(value[3])
    print("compra modificada")


def ver_compras():
    contra = "ADMIN01"

    while True:
        password = input("Ingrese la contraseña")
        if password != contra:
            print("Contraseña Invalida.")
        else:
            break
    print("Acesso concedido")
    time.sleep(1)
    for key, value in compra.items():
        print(
            f"El alumno {value[0]} de {value[1]}, con id: {key}: compró: {value[len(value) - 1]} y pagó con {value[2]}")


def eliminar_compra():
    legajo = input("Ingrese su legajo ")
    if len(compra) == 0:
        print("problemas")
    if legajo in compra:
        del compra[legajo]
    print("Compra eliminada")
