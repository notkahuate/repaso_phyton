# Solicitar la calificación del estudiante
calificacion = float(input("Ingrese la calificación del estudiante (0-100): "))

# Preguntar si hizo tareas adicionales
tareas_adicionales = input("¿Hizo tareas adicionales? (sí/no): ").strip().lower()

# Calcular la calificación final
if tareas_adicionales == "sí":
    # Añadir un 5% extra a la calificación
    calificacion_final = calificacion * 1.05
    # Ajustar la calificación para que no exceda 100
    if calificacion_final > 100:
        calificacion_final = 100
else:
    calificacion_final = calificacion

# Mostrar la calificación final
print(f"La calificación final del estudiante es: {calificacion_final:.2f}")
