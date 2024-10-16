#Escribe un programa que solicite al usuario ingresar su calificación en un examen y determine si ha aprobado o no. 
# Si la calificación es igual o mayor a 60, muestra el mensaje "Has aprobado".
# De lo contrario, muestra el mensaje "Has reprobado"
def calificacion(nota):
    if nota<60 :
        print('ustde reprobo la nota')
    else:
        print('usted aprobo')

if(__name__ == '__main__'):
    nota = int(input('Ingrese la nota  : '))
    calificacion(nota)