# Escribe un programa que solicite al usuario ingresar un número y luego muestre la tabla
#de multiplicar de ese número del 1 al 10
def tabla(num):
    print (f'tabla del numero {num}')
    for i in range (1,11) :
        result = i * num
        print (f'{num} * {i} = {result} ')



if(__name__ == '__main__'): 
    num = int(input('ingrese el numero : '))
    tabla(num)