# Solicitar al usuario que ingrese una calificación numérica
calificacion = float(input("Ingrese la calificación numérica (0-100): "))

# Determinar la letra de la calificación usando match
match calificacion:
    case _ if 90 <= calificacion <= 100:
        letra = "A"
    case _ if 80 <= calificacion < 90:
        letra = "B"
    case _ if 70 <= calificacion < 80:
        letra = "C"
    case _ if 60 <= calificacion < 70:
        letra = "D"
    case _ if 0 <= calificacion < 60:
        letra = "F"
    case _:
        letra = "Calificación fuera del rango válido."

# Mostrar la letra de la calificación
print(f"La calificación en letra es: {letra}")
