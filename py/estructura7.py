# Solicitar al usuario el valor de inicio y el valor de fin
inicio = int(input("Ingrese el valor de inicio: "))
fin = int(input("Ingrese el valor de fin: "))

# Usar un ciclo for para imprimir todos los números pares en el rango
for i in range(inicio, fin + 1):
    if i % 2 == 0:
        print(i)
