import random

print("Bienvenid@ a mi juego del Ahorcado.")

palabras = ['celular', 'ecuador', 'elefante', 'computador', 'audifonos', 'casa', 'teclado', 'programacion']

palabrasecreta = random.choice(palabras)
palabraoculta = "_" * len(palabrasecreta)

intentos = 0
letrasadivinadas = []
while intentos < 6:

    letra = input("Adivina una letra: ")
    if letra in letrasadivinadas:
        print("Ya usaste esa letra, ¡Adivina otra!")
    elif letra in palabrasecreta:
        for i in range(len(palabrasecreta)):
            if palabrasecreta[i] == letra:
                palabraoculta = palabraoculta[:i] + letra + palabraoculta[i+1:]
        print("¡Bien hecho! La palabra es:", palabraoculta)
        if "_" not in palabraoculta:
            print("¡Felicidades, adivinaste la palabra!, deseas volver a jugar ? ")
            break
    else:
        intentos += 1
        print("La letra no se encuentra, elige una nueva te quedan", 6-intentos, "intentos.")
        letrasadivinadas.append(letra)