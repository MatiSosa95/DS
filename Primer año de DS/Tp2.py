import math as m

def ejercicio1():
    lapices= 150
    personas=7
    cantLapicesPorCadaPersona= lapices//personas
    cantSobrantes= lapices%personas
    print(f"La cantidad de lapices que usa cada persona es de {cantLapicesPorCadaPersona} y sobran {cantSobrantes}")

def ejercicio2():
    personas = 7
    lapicesParaCadaUna=15
    cantDeLapicesCaja= 12
    cantDeCajasParaComprar= (personas*lapicesParaCadaUna)/cantDeLapicesCaja
    cantDeCajasParaComprar= m.ceil(cantDeCajasParaComprar)
    print(f"La cantidad de cajas a comprar es de {cantDeCajasParaComprar}")

def ejercicio3():
    radioEsfera1= 5
    radioEsfera2= 12.5
    volumenEsfera1= (4/3)* m.pi* m.pow(radioEsfera1,3)
    volumenEsfera2 = (4 / 3) * m.pi * m.pow(radioEsfera2, 3)
    diferenciaEntreAmbosVolumenes= volumenEsfera2-volumenEsfera1
    print(f"El volumen de la esfera 1 es de {volumenEsfera1} y de la esfera 2 es de {volumenEsfera2}. Mientras que su diferencia de volumen es de {diferenciaEntreAmbosVolumenes}")

def ejercicio4():
    minutosAlDia= 24*60
    diasEnUnAnio= 365
    diasEnUnMes=30

    minutosTotales= int(input("Ingrese los minutos "))

    diasTotales= minutosTotales//minutosAlDia
    anios= diasTotales//diasEnUnAnio
    dias_restantes= diasTotales % diasEnUnAnio

    meses= dias_restantes//diasEnUnMes

    dias= dias_restantes%diasEnUnMes

    print(f"{minutosTotales} minutos equivalen a aproximadamente {anios} años, {meses} meses y {dias} dias ")

def ejercicio5():

    lado1= float(input("ingrese el valor del lado 1 "))
    lado2=float(input("ingrese el valor del lado 2 "))

    print(f"La hipotenusa es: {m.hypot(lado1, lado2)}")

def ejercicio6():
    angulo = float(input("ingrese el valor del angulo "))
    angulo= m.radians(angulo)

    print(f"el seno de {angulo} es: {m.sin(angulo)}")
    print(f"el conseno del {angulo} es: {m.cos(angulo)}")
    print(f"La tangente del {angulo} es: {m.tan(angulo)}")

def desafio():
    BOTELLA= 0.75
    MEDIDAESTANDAR=0.175
    VINOPORCAJA= 6
    PERSONAS=21
    PERSONASQUENOTOMANALCOHOL=3

    vasos_por_botella= int(BOTELLA//MEDIDAESTANDAR)
    vino_restante=BOTELLA%MEDIDAESTANDAR
    alcoholicos=PERSONAS-PERSONASQUENOTOMANALCOHOL
    total_copas_vino=alcoholicos*4

    cant_botellas= (total_copas_vino*MEDIDAESTANDAR)/BOTELLA
    cant_botellas= m.ceil(cant_botellas)
    cant_cajas= cant_botellas/6
    cant_cajas=m.ceil(cant_cajas)
    botellas_vino_restante= cant_cajas*VINOPORCAJA-cant_botellas

    print(f" a- Cantidad de vasos llenos por botellas {vasos_por_botella}")
    print(f" b- vino restante por botella {vino_restante:.2f}")
    print(f" c-La cantidad de personas que asistiran es de {PERSONAS}")
    print(f"d- Personas que no toman alcohol son {PERSONASQUENOTOMANALCOHOL}, por lo tanto las que toman alcohol son {alcoholicos}")
    print(f" e) I- Se necesitaran {cant_botellas} botellas y {cant_cajas} cajas")
    print(f" e) II- Se necesitaran -- botellas y -- cajas")
    print(f" e) III- Quedaran {botellas_vino_restante} botellas restantes")

desafio()

