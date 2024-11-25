# Preguntas de examenes: Modulos= libreria= biblioteca
#las cadenas f tmb pueden ingresarse en las entradas de datos
#para que me servian las cadenas f y cual es la diferencia con ...las cdenas f se puede agregar en la misma expresion las variables
#



a ='facultad'
b = 2024
c = 20.21
print(type(a), type(b), type(c))
print('a= ', a, ',b = ', b, ', c= ', c)

nombre = "Matias"
legajo = 40299
print(f"Me llamo {nombre} y mi legajo es {legajo}.")

name= input("Ingrese su nombre\n")
print(f"Ingrese su apellido {name}")
apellido= input()
print(f"su nombre completo es {name} {apellido}")

nacim = int(input("Introduzca su año de nacimiento\n"))
actual = 2024
edad = 2024 - nacim
print(f"Usted tiene {edad} años")

AmigosdeSilvina = "Pablo Florencia Lucas Andrea Silvana"
separador =" "
usandosplit = AmigosdeSilvina.split(separador)
print ("Mi lista de amigos", usandosplit)
