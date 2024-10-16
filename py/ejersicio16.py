# Solicitar al usuario la distancia y la velocidad promedio
distancia = float(input("Ingrese la distancia a recorrer (en km): "))
velocidad_promedio = float(input("Ingrese la velocidad promedio del automóvil (en km/h): "))

# Verificar si la velocidad promedio es mayor a 120 km/h y mostrar una advertencia
if velocidad_promedio > 120:
    print("Advertencia: La velocidad promedio es mayor a 120 km/h.")

# Calcular el tiempo de viaje en horas
tiempo_horas = distancia / velocidad_promedio

# Convertir el tiempo a horas y minutos
horas = int(tiempo_horas)
minutos = int((tiempo_horas - horas) * 60)

# Mostrar el resultado
print(f"El tiempo estimado de viaje es: {horas} horas y {minutos} minutos.")
