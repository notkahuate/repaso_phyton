#En su casa le solicitan que realice un algoritmo en Python, que permita calcular el valor a pagar por concepto de energía eléctrica. Los datos que se
#conocen son los siguientes:-Mes de consumo-Valorkw -Totalkwconsumido en el mes-estrato
def calcular_valor_energia(mes, valor_kw, total_kw, estrato):
    # Definir porcentaje de ajuste según el estrato (basado en posibles subsidios o incrementos)
    if estrato == 1:
        ajuste = 0.60  # 60% de descuento
    elif estrato == 2:
        ajuste = 0.85  # 15% de descuento
    elif estrato == 3:
        ajuste = 1.0  # Sin descuento ni incremento
    elif estrato == 4:
        ajuste = 1.05  # 5% de incremento
    elif estrato == 5:
        ajuste = 1.10  # 10% de incremento
    elif estrato == 6:
        ajuste = 1.15  # 15% de incremento
    else:
        ajuste = 1.0  # Estrato no válido, sin ajuste

    # Calcular el valor bruto de la energía consumida
    valor_bruto = total_kw * valor_kw

    # Aplicar el ajuste según el estrato
    valor_ajustado = valor_bruto * ajuste

    return valor_ajustado

# Solicitar la información al usuario
mes = input("Ingresa el mes de consumo: ")
valor_kw = float(input("Ingresa el valor por kilovatio (valorKw): "))
total_kw = float(input("Ingresa el total de kilovatios consumidos en el mes (totalKwConsumido): "))
estrato = int(input("Ingresa el estrato: "))

# Calcular el valor a pagar
valor_pagar = calcular_valor_energia(mes, valor_kw, total_kw, estrato)

# Mostrar el valor a pagar
print(f"\nEl valor a pagar por el consumo de energía en {mes} es: ${valor_pagar:.2f}")
