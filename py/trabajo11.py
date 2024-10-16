

def es_triangulo_valido(a, b, c):
    # Verificar la desigualdad triangular
    return a + b > c and a + c > b and b + c > a

# Solicitar al usuario ingresar las longitudes de los lados
a = float(input("Ingresa la longitud del lado a: "))
b = float(input("Ingresa la longitud del lado b: "))
c = float(input("Ingresa la longitud del lado c: "))

# Verificar si los lados pueden formar un triángulo válido
if es_triangulo_valido(a, b, c):
    print("Las longitudes ingresadas pueden formar un triángulo válido.")
else:
    print("Las longitudes ingresadas no pueden formar un triángulo.")
