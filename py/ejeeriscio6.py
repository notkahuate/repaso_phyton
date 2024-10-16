import random

# Generar un número aleatorio entre 1 y 10
num_Adivinar = random.randint(1, 10)

# Bucle para que el usuario intente adivinar el número
while True:
    # Solicitar al usuario que ingrese un número
    num_Intento = int(input("Adivina el número (entre 1 y 10): "))
    
    # Comparar el número ingresado con el número aleatorio
    if num_Intento < num_Adivinar:
        print("El número es mayor. Intenta nuevamente.")
    elif num_Intento > num_Adivinar:
        print("El número es menor. Intenta nuevamente.")
    else:
        print("¡Felicidades! Adivinaste el número.")
        break  # Terminar el juego si el número es correcto
