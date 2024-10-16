# Solicitar al usuario que ingrese un año
año = int(input("Ingrese un año: "))

# Determinar si el año es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
