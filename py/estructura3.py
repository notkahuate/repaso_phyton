# Solicitar al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Inicializar el factorial como 1
factorial = 1

# Usar un ciclo for para calcular el factorial del número
for i in range(1, n + 1):
    factorial *= i

# Mostrar el resultado
print(f"El factorial de {n} es: {factorial}")
