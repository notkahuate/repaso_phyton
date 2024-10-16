# Inicializar la suma de números pares
suma_pares = 0

# Usar un ciclo while para ingresar números indefinidamente
while True:
    numero = int(input("Ingrese un número entero: "))
    
    # Verificar si el número es impar y detener el ciclo si es así
    if numero % 2 != 0:
        break
    
    # Sumar el número si es par
    suma_pares += numero

# Mostrar el resultado
print(f"La suma de los números pares ingresados es: {suma_pares}")
