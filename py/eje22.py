# Solicitar al usuario los tres ángulos del triángulo
angulo1 = float(input("Ingrese el primer ángulo del triángulo (en grados): "))
angulo2 = float(input("Ingrese el segundo ángulo del triángulo (en grados): "))
angulo3 = float(input("Ingrese el tercer ángulo del triángulo (en grados): "))

# Verificar si los ángulos forman un triángulo válido
if angulo1 + angulo2 + angulo3 != 180:
    print("Los ángulos ingresados no forman un triángulo válido.")
else:
    # Clasificar el triángulo según sus ángulos
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        tipo_triangulo = "rectángulo"
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        tipo_triangulo = "obtuso"
    else:
        tipo_triangulo = "agudo"

    # Mostrar el tipo de triángulo
    print(f"El triángulo es {tipo_triangulo}.")
