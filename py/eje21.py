# Solicitar al usuario el número de horas de estacionamiento
horas = float(input("Ingrese el número de horas de estacionamiento: "))

# Inicializar el costo total
costo_total = 0

# Calcular el costo basado en las tarifas progresivas
if horas > 0:
    # Primera hora
    costo_total += 5
    
    # Segunda a cuarta hora
    if horas > 1:
        horas_restantes = min(horas - 1, 3)
        costo_total += horas_restantes * 4
    
    # Más de cuatro horas
    if horas > 4:
        horas_adicionales = horas - 4
        costo_total += horas_adicionales * 3
else:
    print("El número de horas debe ser mayor que 0.")

# Mostrar el costo total
print(f"El costo total de estacionamiento es: ${costo_total:.2f}")
