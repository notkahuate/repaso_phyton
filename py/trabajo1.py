#Escribe un programa que solicite al usuario ingresar su edad y luego determine si es mayor de edad o no
#utilizando una declaraciónif. Si la edades mayor o igual a 18, muestra el mensaje "Eres mayor de edad", de lo
#contrario, muestra el mensaje "Eres menor de edad".
def  mayormenor(edad:int) :

    if edad>18 :
        print('usted es mayor de edad')
    else :
        print('ustde es menor de edad')


if(__name__ == '__main__'):
    edad = int(input('ingrese la edad : '))
    mayormenor(edad)