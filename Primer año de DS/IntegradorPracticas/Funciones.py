import time

juego = {
    "El sol es una estrella ubicada en el centro de nuestro sistema solar": "V",
    "Los delfines son mamíferos y no peces": "V",
    "La Gran Muralla China es visible desde el espacio a simple vista": "F",
    "La luz viaja más rápido en el agua que en el aire": "F",
    "La Antártida es el continente con el clima más cálido": "F",
    "Todos los pingüinos viven en climas fríos": "F",
    "Shakespeare escribió más de 50 obras de teatro": "F",
    "El ser humano tiene más huesos al nacer que en la adultez": "V",
    "Las jirafas tienen el mismo número de vértebras en el cuello que los humanos": "V",
    "Albert Einstein ganó el Premio Nobel de Física por su teoría de la relatividad": "F",
    "Los lenguajes de programación más utilizados en Argentina son: Python, JavaScript, y Java": "V",
    "Luis Scola, Andrés Nocioni son reconocidos beisbolistas argentinos": "F",
    "Christopher Lloyd dirigio 'Volver al futuro' en 1995": "F",
    "Lionel Messi actualmente es jugador de Inter de Milan" :  "F",
    "Un ejemplo de hardware es el sistema operativo Windows" : "F"
}
score_total = {}
nombre_jugador = ""

def jugar():
    puntaje = 0
    texto = """
            ┌──────────────────────────────────────────┐
            │ ████████ █████   ██ ██    ██ ██   ██     │
            │    ██    ██   ██ ██ ██    ██ ██  █████   │
            │    ██    ██   ██ ██ ██    ██ ██ ██   ██  │
            │    ██    █████   ██ ██    ██ ██ ██   ██  │
            │    ██    ██  ██  ██  ██  ██  ██ ███████  │
            │    ██    ██   ██ ██    ██    ██ ██   ██  │
            └──────────────────────────────────────────┘ """
    bienvenida= """ 
    Obtienes 10 puntos por cada respuesta correcta
    
    HORA DE COMENZAR CON LA TRIVIA... ¡¡MUCHA SUERTE!!"""
    time.sleep(1)
    if len(juego)==0:
        print("Juego inexistente")
        return 0
    else:
        for line in texto.splitlines():
            print(line)
            time.sleep(0.1)
        print(bienvenida)

        for k, v in juego.items():
            print("=" * len(k))
            print(k)
            print("=" * len(k))
            respuesta = input("Elija V para Verdadero y F para Falso ")
            if respuesta.upper() == v:
                print("Correcto. Obtienes 10 puntos")
                puntaje += 10
            else:
                print(f"Incorrecto. La respuestas para {k} es {v}")
        time.sleep(0.5)
        nombre_jugador = input("Ingrese su nombre ")
        if nombre_jugador in score_total.keys():
            nombre_jugador = input("Ya existe ese nombre de Jugador.Ingrese otro nombre")
        score_total[nombre_jugador] = f"{puntaje} puntos"
        return puntaje


def CrearJuego():
    respuesta = "s"
    trivia = ""
    while respuesta.lower() == "s":
        print("ingresar trivias para el juego ")
        trivia = input("trivia: ").lower()
        solucion = input("Solucion: ").upper()
        while solucion not in ["V", "F", ""]:
            solucion= input("ERROR, ingrese 'V' para verdadero o 'F' para falso  ").upper()
        juego[trivia] = solucion.upper()
        respuesta = input("¿Quiere ingresar más trivias o cuestionarios? (s/n): ").lower()
        while respuesta not in ["s", "n"]:
            print("Respuesta no valida, ingrese 's' para si o 'n' para no")
            respuesta = input("¿Quiere ingresar más trivias o cuestionarios? (s/n): ").lower()

        # Mostrar Trivias

    print("\nDiccionario de Trivias ingresadas:")

    for i, (clave, valor) in enumerate(juego.items(), start=1):
        print(f"Trivia nª{i} :{clave} / Solución:{valor}")


def ModificarTrivia():
    print("\nModificar una trivia")
    print("\nPreguntas disponibles en el juego:")
    si= True

    while si:
        for i, pregunta in enumerate(juego.keys(), 1):
            print(f"{i}. {pregunta}")

        trivia = input("Ingrese la trivia, tal y como está escrita, que desea modificar: ")

        if trivia in juego:
            nueva_trivia = input("Ingrese la nueva trivia (Enter para no cambiar): ").lower()
            nueva_solucion = input("Ingrese la nueva solución V o F (Enter para no cambiar): ").upper()

            # Si no ingresa nada no se modifica ninguna trivia
            if nueva_trivia:
                juego[nueva_trivia] = juego.pop(trivia)  # Cambia la clave/premisa de la trivia
            while nueva_solucion!="F" and nueva_solucion!="V":
                if nueva_solucion in ["V", "F"]:
                    juego[nueva_trivia or trivia] = nueva_solucion  # Cambia la solución de la trivia
                else:
                    nueva_solucion= input("Opcion Erronea. Digite V o F ").upper()
                    juego[nueva_trivia or trivia] = nueva_solucion

            print("\nTrivia modificada correctamente.")
        else:
            print("La trivia no se encontró en el diccionario.")
        opcion= input("desea seguir modificando el juego?(s/n)" )
        if opcion.lower()=="n":
            si=False
        elif opcion.lower()=="s":
            si=True
        else:
            print("Opcion Incorrecta")


def EliminarJuego():
    juego.clear()
    print("Eliminando Juego", end="")
    escribir_lento("...")
    print("Juego Eliminado")

def EliminarPreguntas():
    si=True
    while si:
        for k, v in juego.items():
            print(f"Pregunta: {k}")
        pregunta = input("¿Qué trivia quiere modificar? Escriba la trivia tal y como está: ")
        time.sleep(1)
        if pregunta in juego.keys():
            juego.pop(pregunta)
            print(f"Ud. ha eliminado la pregunta con exito")
        else:
            print("No has ingresado preguntas para modificar")

        time.sleep(0.5)
        opcion=input("¿Desea modificar otra trivia?(s/n)")
        if opcion=="n":
            si=False
        elif opcion=="s":
            si=True
        else:
            print("Opcion Incorrecta")

    return juego

def Puntaje():
    print("""
    ====================
            PUNTAJE 
    ====================""")
    if len(score_total) == 0:
        print("    No existen jugadores")
    else:
        for k, v in score_total.items():
            print(f"    {k} obtuvo:{v}")


def Instrucciones():
    intrucciones= """
    
Trivia - Instrucciones ℹ️  
=============================  
Opciones del Menú:
=============================  
1➡ Jugar: Responde las trivias predeterminadas y al finalizar ingresa su nombre para luego verlo reflejado cuanto los puntajes.
2➡ Crear tu propio Juego: Personaliza la trivia agregando nuevas preguntas.
3➡ Modificar Trivia: Reemplazar preguntas específicas dentro de la trivia.
4➡ Eliminar Juego: Eliminando todas las preguntas.
5➡ Eliminar Preguntas: Elimina una pregunta específica de la trivia.
6➡ Ver Puntaje: Consulta el ranking de jugadores con sus puntajes actuales.
7➡ Instrucciones: Podes revisar las instrucciones en cualquier momento.
8➡ Salir: Finalizar el juego """
    salir = True
    while salir:
        print(intrucciones)
        opcion = input("Desea salir al menú principal? (s/n) ")
        if opcion.lower() == "s":
            salir = False
        elif opcion.lower() == "n":
            salir = True
        else:
            print("Opcion incorrecta")


def escribir_lento(texto):
    for letra in texto:
        print(letra, end="")
        time.sleep(0.5)
    print()