import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar la variable para almacenar la suposición del usuario
adivinanza = None

# Usar un ciclo while para permitir al usuario seguir intentando hasta adivinar el número
while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 1 y 100): "))
    
    if adivinanza < numero_secreto:
        print("El número secreto es mayor.")
    elif adivinanza > numero_secreto:
        print("El número secreto es menor.")

print("¡Felicidades! Has adivinado el número.")
