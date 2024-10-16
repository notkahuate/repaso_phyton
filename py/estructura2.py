# Solicitar al usuario una cadena de texto
cadena = input("Ingrese una cadena de texto: ").lower()

# Inicializar el contador de vocales
contador_vocales = 0

# Usar un ciclo for para contar las vocales en la cadena
for caracter in cadena:
    if caracter in 'aeiou':
        contador_vocales += 1

# Mostrar el resultado
print(f"El número de vocales en la cadena es: {contador_vocales}")
