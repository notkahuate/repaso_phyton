#Escribe un programa que solicite al usuario ingresar el día, el mes y el año de
#una fecha. Luego, verifica si la fecha es válida o no. Considera los diferentes
#casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje
#indicando si la fecha es válida o no.
def fecha(day, month, year):
    # Verificar si el año es válido
    if year > 0 and year < 2024:
        
        # Verificar si el año es bisiesto
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            bisiesto = True
        else:
            bisiesto = False

        # Verificar si el mes es válido
        if month >= 1 and month <= 12:

            # Meses con 31 días
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if day >= 1 and day <= 31:
                    print(f'{day}/{month}/{year} es una fecha válida')
                else:
                    print('Ingrese un día válido para un mes de 31 días')

            # Meses con 30 días
            elif month in [4, 6, 9, 11]:
                if day >= 1 and day <= 30:
                    print(f'{day}/{month}/{year} es una fecha válida')
                else:
                    print('Ingrese un día válido para un mes de 30 días')

            # Febrero (mes 2)
            else:
                if bisiesto:
                    if day >= 1 and day <= 29:
                        print(f'{day}/{month}/{year} es una fecha válida (año bisiesto)')
                    else:
                        print('Ingrese un día válido para febrero en un año bisiesto')
                else:
                    if day >= 1 and day <= 28:
                        print(f'{day}/{month}/{year} es una fecha válida')
                    else:
                        print('Ingrese un día válido para febrero en un año no bisiesto')

        else:
            print('Ingrese un mes válido')

    else:
        print('Ingrese un año válido')

if __name__ == '__main__':
    day = int(input('Ingrese el día: '))
    month = int(input('Ingrese el mes: '))
    year = int(input('Ingrese el año: '))
    fecha(day, month, year)
