import time,IOError, Funciones as F

menu= """
=============================
    Juego de la Trivia 
=============================
El objetivo es responder a una serie de enunciados indicando si son verdaderos o falsos con “v” o “f”.
Para comenzar, revisa las instrucciones si es la primera vez que juegas.

Seleccione una opción:
=============================
  1- Jugar
  2️- Crear tu propio Juego
  3️- Modificar el juego
  4️- Eliminar el juego completamente
  5️- Eliminar parte del juego
  6️- Ver puntaje
  7️- Instrucciones
  8️- Salir
=============================

Programa Creado por Sosa Matias y Gonzalez Nicolás\n"""
try:
    opcion = int(input(menu))

    puntaje = 0
    while opcion != 8:
        if opcion == 1:
            puntaje = F.jugar()
            print(f"Tu puntaje es: {puntaje}")
        elif opcion == 2:
            F.CrearJuego()
            time.sleep(1.5)
        elif opcion == 3:
            F.ModificarTrivia()
            time.sleep(1.5)
        elif opcion == 4:
            F.EliminarJuego()
            time.sleep(1.5)
        elif opcion == 5:
            F.EliminarPreguntas()
            time.sleep(1.5)
        elif opcion == 6:
            F.Puntaje()
            time.sleep(1.5)
        elif opcion == 7:
            F.Instrucciones()
            time.sleep(1.5)
        else:
            print("Opcion Incorrecta")
        opcion = int(input(menu))
except:
    IOError.error_de_entrada()

print("Saliendo", end="")
F.escribir_lento("...")