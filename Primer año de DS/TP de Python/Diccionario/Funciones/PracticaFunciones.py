def suma(a,b):
    return a+b

def suma_media(a,b,c):
    suma= a+b+c
    media=suma/3
    return suma, media

#Argumentos por nombre
def multiplicacino(b,a):
    return a*b

#Argumento por defecto
def suma3(a, b, c=0):
    return a+b+c

print(suma(500,1000))
suma1,media1= suma_media(1,2,3)
print(suma1)
print(media1)
print(multiplicacino(a=50, b=10))
print(suma3(2,3,6))
print(suma3(3,3))#No da error al enviar 2 valores, porque c esta inicializada con 0