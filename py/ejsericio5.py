# Solicitar un número del 1 al 7
numero = int(input("Ingrese un número del 1 al 7: "))

# Usar match para mostrar el día de la semana correspondiente
match numero:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número no válido. Por favor, ingrese un número del 1 al 7.")