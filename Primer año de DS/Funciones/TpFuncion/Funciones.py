def ManejodeVocales(frase):
    vocales = "aeiouáéíóú"
    cant_vocales=0
    frase= frase.lower()
    for i in range(len(frase)):
        if frase[i] in vocales:
            cant_vocales+=1
            print(f"En el caracter {i+1} esta la vocal {frase[i]}")
    return cant_vocales

def ManejodeConsonantes(frase):
    consonantes= "bcdfghjkmnñlpqrstvwxyz"
    cant_consonantes= 0
    frase = frase.lower()
    for consonante in frase:
        if consonante in consonantes:
            cant_consonantes+=1

    return cant_consonantes