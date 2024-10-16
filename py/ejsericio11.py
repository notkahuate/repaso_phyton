# Solicitar al usuario que ingrese una temperatura y la escala
temperatura = float(input("Ingrese la temperatura: "))
escala = input("Ingrese la escala de la temperatura (C para Celsius, F para Fahrenheit): ").upper()

# Usar match para realizar la conversión
match escala:
    case 'C':
        # Convertir de Celsius a Fahrenheit
        temperatura_fahrenheit = (temperatura * 9/5) + 32
        print(f"{temperatura}°C es igual a {temperatura_fahrenheit}°F")
    case 'F':
        # Convertir de Fahrenheit a Celsius
        temperatura_celsius = (temperatura - 32) * 5/9
        print(f"{temperatura}°F es igual a {temperatura_celsius}°C")
    case _:
        print("Escala no válida. Por favor ingrese 'C' o 'F'.")
        
