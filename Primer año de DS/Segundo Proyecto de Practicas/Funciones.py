import  Reglas
juego = {
    "El sol es una estrella ubicada en el centro de nuestro sistema solar": "V",
    "Los delfines son mamíferos y no peces": "V",
    "La Gran Muralla China es visible desde el espacio a simple vista": "F",
    "La luz viaja más rápido en el agua que en el aire": "F",
    "La Antártida es el continente con el clima más cálido": "F",
    "Todos los pingüinos viven en climas fríos": "F",
    "Shakespeare escribió más de 50 obras de teatro.": "F",
    "El ser humano tiene más huesos al nacer que en la adultez": "V",
    "Las jirafas tienen el mismo número de vértebras en el cuello que los humanos": "V",
    "Albert Einstein ganó el Premio Nobel de Física por su teoría de la relatividad": "F"
}
score_total = {}
nombre_jugador = ""

def jugar():
    puntaje = 0
    for k, v in juego.items():
        print(k)
        respuesta = input("Elija V para Verdadero y F para Falso.")
        if respuesta.upper() == v:
            print("Correcto")
            puntaje += 10
        else:
            print(f"Incorrecto. La respuestas para {k} es {v}")
    nombre_jugador= input("Ingrese su nombre")
    score_total[nombre_jugador]=f"{puntaje} puntos"
    return puntaje


def CrearJuego():
    respuesta = "s"
    trivia = ""
    while respuesta.lower() == "s":
        print("ingresar trivias para el juego ")
        trivia = input("trivia ").lower()
        solucion = ""
        while solucion.lower() not in ["v", "f"]:
            solucion = input("resolución (v/f) ").upper()
            if solucion not in ["V", "F"]:
                print(" ERROR, ingrese 'V' para verdadero o 'F' para falso  ")
        juego[trivia] = solucion
        respuesta = input("¿Quiere ingresar más trivias o cuestionarios? (s/n): ").lower()
        # Mostrar Trivias

    print("\nDiccionario de Trivias ingresadas:")

    for i, (clave, valor) in enumerate(juego.items(), start=1):
        print(f"Trivia nª{i} :{clave} / Solución:{valor}")
    return juego


def ModificarTrivia():
    print("\nModificar una trivia")
    for k, v in juego.items():
        print(f"Pregunta: {k}, respuesta: {v}")

    trivia = input("Ingrese la trivia que desea modificar: ")

    if trivia in juego:
        nueva_trivia = input("Ingrese la nueva trivia (Enter para no cambiar): ").lower()
        nueva_solucion = input("Ingrese la nueva solución (Enter para no cambiar): ").upper()

        # Si no ingresa nada no se modifica ninguna trivia
        if nueva_trivia:
            juego[nueva_trivia] = juego.pop(trivia)  # Cambia la clave/premisa de la trivia
        if nueva_solucion:
            juego[nueva_trivia or trivia] = nueva_solucion  # Cambia la solución de la trivia

        print("\nTrivia modificada correctamente.")
    else:
        print("La trivia no se encontró en el diccionario.")


def EliminarJuego():
    juego.clear()


def EliminarPreguntas():
    for k, v in juego.items():
        print(f"Pregunta: {k} Respuesta: {v}")

    pregunta= input("¿Qué pregunta quiere modificar? Escriba la pregunta tal y como está ")
    if pregunta in juego.keys():
        print(f"Ud. ha eliminado con exito {pregunta}")
        juego.pop(pregunta)
    else:
        print("No se encontró la pregunta a modificar")

    return juego

def Puntaje():
    if len(score_total) == 0:
        print("No hay jugadores")
    else:
        for k, v in score_total.items():
            print(f"{k}:{v}")

def reglas():
    Reglas.reglas()