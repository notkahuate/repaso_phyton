#Crea un programa que solicite al usuario ingresar una serie de números positivos y luego calcule e imprima el promedio de los
# números ingresados utilizando un bucle while. El programa debe terminar cuando el usuario ingrese un número negativo.
def promedio():
    total = 0
    contador = 0

    numero = int(input('ingrese un numero : '))

    while numero > 0 :
        total += numero
        contador += 1
        numero = int(input('ingrese un numero : '))
    
    promedio = total/contador

    print (f' el promedio seria de : {promedio}')

    
if(__name__ == '__main__'): 
    promedio()


