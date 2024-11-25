preguntas = {
    '¿cual es la capital de Francia?': {
        'A': 'Berlin',
        'B': 'Paris',
        'C': 'Londres',
        'D': 'Roma'
    },
    '¿cual es el planeta mas cercano al sol?': {
        'A': 'Mercurio',
        'B': 'Venus',
        'C': 'Tierra',
        'D': 'Marte'
    },
    '¿cual es el pais mas poblado del mundo?': {
        'A': 'India',
        'B': 'Estados Unidos',
        'C': 'China',
        'D': 'Colombia'
    }
}
respuestas_correctas = {
    '¿cual es la capital de Francia?': 'B',
    '¿cual es el planeta mas cercano al sol?': 'A',
    '¿cual es el pais mas poblado del mundo?': 'C'
}

for pregunta, opciones in preguntas.items():
    print(pregunta)
    for num, ans in opciones.items():
        print(f'{num}:{ans}')
    respuesta = input('escribe tu respuesta:')
    if respuesta.upper() == respuestas_correctas[pregunta]:
        print('respuesta correcta')
    else:
        print('respuesta incorrecta')
        break