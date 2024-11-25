import random

# Definir los caracteres válidos y la longitud de la cadena
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789¿?¡!#$%&/()=/-_,;:."
longitud = 10
cadena_aleatoria=""
# Crear la cadena aleatoria
for _ in range(longitud):
    cadena_aleatoria += random.choice(caracteres)

print(cadena_aleatoria)

for i in range(10):
    print(i)