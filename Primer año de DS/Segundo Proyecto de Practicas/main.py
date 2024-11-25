import time
import Funciones as F

menu= """
Trivia 
1-Jugar
2-Crear tu propio Juego -> Alta, Baja total, Baja Parcial, modificacion a partir de preguntas
3-Modifica el juego 
4-Eliminar totalmente el juego
5-Elimina parcialmente parte del juego
6-Ver puntaje ->Un diccionario con el nombre del jugador y el puntaje -> Va a poder eliminar parcial o totalmente el puntaje
7-Intrucciones
8-Salir

Programa Creado por Colapinto\n"""
opcion= int(input(menu))
puntaje=0
diccionario={}#borrar esto
while opcion!=8:
    if opcion==1:
        puntaje=F.jugar()
        print(f" Tu puntaje es: {puntaje}")
    if opcion == 2:
        F.CrearJuego()
    if opcion==3:
        F.ModificarTrivia()
    if opcion==4:
        F.EliminarJuego()
    if opcion==5:
        F.EliminarPreguntas()
    if opcion==6:
        F.Puntaje()
    if opcion==7:
        F.reglas()
    opcion = int(input(menu))

print("Saliendo",end="")
time.sleep(0.5)
print(".",end="")
time.sleep(.5)
print(".",end="")
time.sleep(.5)
print(".",end="")
time.sleep(.5)