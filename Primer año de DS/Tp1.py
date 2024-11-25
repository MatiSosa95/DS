

def Ejercicio1():
    print("El verdadero desafío es imaginarte el algoritmo y no programarlo")

def Ejercicio2():
    nickname="Arigaruton" #String
    cumple="08 de Marzo de 1995" #string
    edad=29 #Integer
    factura="Cuota del Gimnasio" #String
    compra= 15000.00 #float

    print(f"{nickname} es del tipo", type(nickname))
    print(f"{cumple} es del tipo", type(cumple))
    print(f"{edad} es del tipo" , type(edad))
    print(f"{factura} es del tipo" , type(factura))
    print(f"{compra} es del tipo" , type(compra))

def Ejercicio3():
    materiaPreferida= input("Ingrese su materia favorita\n")
    pasatiempo= input("Ingrese su pasatiempo\n")
    deporte= input("Ingrese el deporte que hace\n")
    familia= int(input("Ingrese cuantas personas compone su familia\n"))
    nroDeMascotas= int(input("Ingrese cuantas mascotas tiene\n"))

    print(f"Mi materia preferida en el colegio es {materiaPreferida}. Mi pasatiempo preferido es {pasatiempo}. Practico {deporte} como "
          f"deporte. En mi familia somos {familia} personas y {nroDeMascotas} mascotas")

def Ejercicio4():
    nickname= "matias sosa"
    print(nickname[0:6].lower().capitalize() +" "+ nickname[6:11].upper())

def desafio():
    nombre = "Matias"
    apellido = "Sosa"
    nombredelestudiante = "Este es el trabajo de: apellido,nombre"
    nombredelestudiante = nombredelestudiante.replace("apellido", apellido).replace("nombre", nombre)

    print(nombredelestudiante)

desafio()