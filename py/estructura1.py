# Solicitar al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Inicializar la suma
suma = 0

# Usar un ciclo for para calcular la suma de los primeros n números enteros
for i in range(1, n + 1):
    suma += i

# Mostrar el resultado
print(f"La suma de los primeros {n} números enteros es: {suma}")
