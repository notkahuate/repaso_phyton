# Solicitar al usuario su salario bruto y país de residencia
salario_bruto = float(input("Ingrese su salario bruto: "))
pais = input("Ingrese su país de residencia (País A, País B, País C): ").strip()

# Determinar el porcentaje de impuestos según el país
match pais:
    case "País A":
        porcentaje_impuesto = 0.20
    case "País B":
        porcentaje_impuesto = 0.15
    case "País C":
        porcentaje_impuesto = 0.10
    case _:
        porcentaje_impuesto = 0.25

# Calcular el salario neto
impuesto = salario_bruto * porcentaje_impuesto
salario_neto = salario_bruto - impuesto

# Mostrar el resultado
print(f"Salario bruto: {salario_bruto:.2f}")
print(f"Impuesto aplicado: {impuesto:.2f}")
print(f"Salario neto: {salario_neto:.2f}")
