# Solicitar el número de materias cursadas
num_materias = int(input("Ingrese el número de materias que ha cursado: "))

# Inicializar el contador de créditos
total_creditos = 0

# Procesar cada materia
for i in range(num_materias):
    # Solicitar el puntaje obtenido en la materia
    puntaje = float(input(f"Ingrese el puntaje obtenido en la materia {i + 1}: "))
    
    # Determinar si la materia fue aprobada
    if puntaje >= 60:
        # Cada materia aprobada otorga 3 créditos
        total_creditos += 3
    else:
        print(f"No aprobó la materia {i + 1}.")

# Mostrar el número total de créditos
print(f"El número total de créditos obtenidos es: {total_creditos}")
