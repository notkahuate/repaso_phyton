

def eliminar(nombres):
    while True: 
        ans = input('¿Desea eliminar algún nombre? (1. Sí, 2. No): ')
        
        if ans == '1':  
            nombre_a_eliminar = input("Ingresa el nombre que deseas eliminar: ")
            if nombre_a_eliminar in nombres:
                nombres.remove(nombre_a_eliminar)
                print(f"{nombre_a_eliminar} ha sido eliminado.")
            else:
                print(f"{nombre_a_eliminar} no está en la lista.")
                
        elif ans == '2':
            break  
        
        else:
            print('Por favor, ingrese una opción válida (1 o 2).')

    print(nombres)




def leer_nombres():
    nombres = []
    while True:
        nombre = input("Ingresa un nombre (o presiona Enter para finalizar): ")
        if nombre == "":
            break
        nombres.append(nombre)
    
    if nombres:
        print("\nNombres ingresados:")
        for nombre in nombres:
            print(nombres)
            eliminar(nombres)

    else:
        print("No se ingresaron nombres.")
        


if(__name__ == '__main__'):
    leer_nombres()
         





