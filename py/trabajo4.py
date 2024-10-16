
#Crea un programa que pida al usuario ingresar el nombre de un país y luego
#determine en qué continente se encuentra.Utiliza estructuras condicionales para
#asociar cada país con su respectivo continente y muestra un mensaje con el
#Continente correspondiente.

def contienete(num :int ):
    match num :
        case 1 :
            continente = 'america'
        case 2 :
            continente = 'europa'
        case 3 :
            continente = 'asia'
        case 4 :
            continente = 'oceania'
        case _:
            print('ingrese valor valido') 

    print(f'su continente es {continente}')


if(__name__ == '__main__'):
    print('escoja su pais')
    print('1. colombia 2.españa 3.china 4.australia')
    num =int(input(''))
    contienete(num)


    