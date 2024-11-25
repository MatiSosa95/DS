
def indice_corporal(altura, peso):
    imc=peso/pow(altura/100,2)

    if imc<16:
        print("Tiene desnutricion severa")
    if imc>=16.1 and imc<=18.4:
        print("Tiene desnutricion moderada")
    if imc>=18.5 and imc<=22:
        print("Tiene bajo peso")
    if imc >= 22.1 and imc <= 24.9:
        print("Tiene peso normal")
    if imc >= 25 and imc <= 29.9:
        print("Tiene sobrepeso")
    if imc >= 30 and imc <= 34.9:
        print("Tiene Obecidad tipo 1")
    if imc >= 35 and imc <= 39.9:
        print("Tiene Obecidad tipo 2")
    if imc >39.9:
        print("Tiene Obecidad tipo 3")

def indice_corporal2(altura, peso):
    imc=peso/pow(altura/100,2)

    if imc<16:
        print("Tiene desnutricion severa")
    elif imc<=18.4:
        print("Tiene desnutricion moderada")
    elif imc<=22:
        print("Tiene bajo peso")
    elif  imc <= 24.9:
        print("Tiene peso normal")
    elif imc <= 29.9:
        print("Tiene sobrepeso")
    elif imc <= 34.9:
        print("Tiene Obecidad tipo 1")
    elif imc <= 39.9:
        print("Tiene Obecidad tipo 2")
    elif imc >39.9:
        print("Tiene Obecidad tipo 3")
    else:
        print("Ingresó un valor erroneo")

altura= float(input("Ingrese su altura en centimetros "))
peso= float(input("Ingrese su peso en kilos "))
indice_corporal(altura, peso)
indice_corporal2(altura, peso)
