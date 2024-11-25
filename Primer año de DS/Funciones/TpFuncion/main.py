import Funciones as F
import time

menu= """
Funciones
1-Contar vocales
2-Contar Consonantes
3-Salir\n"""

opcion= int(input(menu))
while opcion!=3:
    if opcion==1 :
        frase = input("Ingrese la frase que quiera manejar ")
        print(F.ManejodeVocales(frase))

    if opcion==2:
        frase = input("Ingrese la frase que quiera manejar ")
        print(F.ManejodeConsonantes(frase))
    opcion = int(input(menu))

print("Saliendo",end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")