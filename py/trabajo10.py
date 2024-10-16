#Construya un algoritmo en Python, que permita ingresar la información de un empleado e imprima el nombre, los apellidos
#y la antigüedad. Los datos que se deben solicitarson los siguientes: *Nombre* Teléfono *Año de ingreso a la empresa*Apellidos *Edad.
def obtener_informacion_empleado(nombre,apellido,telefono,año_ingreso,año_actual,edad):

    # Calcular la antigüedad del empleado
    antigüedad = año_actual - año_ingreso

    # Mostrar la información del empleado
    print("\nInformación del empleado:")
    print(f"Nombre: {nombre}")
    print(f"Apellidos: {apellidos}")
    print(f"Antigüedad en la empresa: {antigüedad} años")

# Ejecutar el algoritmo
# Solicitar la información del empleado
    nombre = input("Ingresa el nombre del empleado: ")
    apellidos = input("Ingresa los apellidos del empleado: ")
    telefono = input("Ingresa el teléfono del empleado: ")
    año_ingreso = int(input("Ingresa el año de ingreso a la empresa: "))
    año_actual = int(input("Ingresa el año actual: "))
    edad = int(input("Ingresa la edad del empleado: "))

    obtener_informacion_empleado(nombre,apellido,telefono,año_ingreso,año_actual,edad)
