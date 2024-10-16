# Programa para verificar si tres longitudes pueden formar un triángulo válido

def es_triangulo_valido(a, b, c):
    return a + b > c and a + c > b and b + c > a


a = float(input("Ingresa la longitud del lado a: "))
b = float(input("Ingresa la longitud del lado b: "))
c = float(input("Ingresa la longitud del lado c: "))


if es_triangulo_valido(a, b, c):
    print("Los lados pueden formar un triángulo válido.")
else:
    print("Los lados no pueden formar un triángulo válido.")