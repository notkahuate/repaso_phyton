# Solicitar dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Solicitar la operación matemática
operacion = input("Ingrese la operación (+, -, *, /): ")

# Usar match para realizar la operación
match operacion:
    case '+':
        resultado = num1 + num2
        print(f"El resultado de {num1} + {num2} es: {resultado}")
    case '-':
        resultado = num1 - num2
        print(f"El resultado de {num1} - {num2} es: {resultado}")
    case '*':
        resultado = num1 * num2
        print(f"El resultado de {num1} * {num2} es: {resultado}")
    case '/':
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de {num1} / {num2} es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero")
    case _:
        print("Operación no válida")
