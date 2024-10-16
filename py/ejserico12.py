# Solicitar al usuario que ingrese su peso y altura
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Clasificar el estado de peso según el IMC
if imc < 18.5:
    estado_peso = "bajo peso"
elif 18.5 <= imc < 25:
    estado_peso = "peso normal"
elif 25 <= imc < 30:
    estado_peso = "sobrepeso"
else:
    estado_peso = "obesidad"

# Mostrar el IMC y el estado de peso
print(f"Tu IMC es: {imc:.2f}")
print(f"Estado de peso: {estado_peso}")
