# Definir la letra secreta
letra_secreta = "A"

# Solicitar al usuario que adivine la letra
letra_adivinanza = input("Adivina la letra secreta: ").upper()

# Verificar si la letra adivinada es correcta
if letra_adivinanza == letra_secreta:
    print("¡Felicidades! Adivinaste la letra secreta.")
else:
    print("Lo siento, la letra adivinada es incorrecta. Intenta nuevamente.")
