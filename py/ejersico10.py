# Solicitar al usuario que ingrese una nota numérica
nota = float(input("Ingrese la nota numérica (0-100): "))

# Clasificar la nota según el rango
if 90 <= nota <= 100:
    calificacion = "A"
elif 80 <= nota < 90:
    calificacion = "B"
elif 70 <= nota < 80:
    calificacion = "C"
elif 60 <= nota < 70:
    calificacion = "D"
elif nota < 60:
    calificacion = "F"
else:
    calificacion = "Nota fuera del rango válido."

# Mostrar la calificación
print(f"La calificación para la nota {nota} es: {calificacion}")
