# Solicitar al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Clasificar a la persona según su edad
if 0 <= edad <= 12:
    print("Eres un niño.")
elif 13 <= edad <= 17:
    print("Eres un adolescente.")
elif 18 <= edad <= 64:
    print("Eres un adulto.")
elif edad >= 65:
    print("Eres un anciano.")
else:
    print("Edad no válida.")