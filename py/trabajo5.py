
#Crea un programa que solicite al usuario ingresar una contraseña y verifique si cumple con los siguientes
# requisitos: debe tener al menos 8 caracteres y contener al menos un número. Si la contraseña cumple con
#los requisitos, muestra el mensaje"Contraseña válida". De lo contrario, muestra el mensaje
"Contraseña inválida".
def check_password(password):
    if len(password) >= 8 and any(char.isdigit() for char in password):
        return "Contraseña válida"
    else:
        return "Contraseña inválida"


if(__name__ == '__main__'):
    password = input('ingrese su contraseña: ')
    print(check_password(password))