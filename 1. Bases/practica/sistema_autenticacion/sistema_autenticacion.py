#Crea un programa de validacion de usuario y contraseña
#Crea 2 constantes con los valores correctos y compara que el usuario y contraseña ingresados por el usuario sean validos
#Debes solicitar el usuario y el password al usuario y si son iwales que los valres correctos almacenados en las constantes,debe imprimir True, de lo contrario debe imprimir False.

import usuarios #Creamos un archivo que contenga usuario y contraseña
def data():
    user = str(input("Username: "))
    contra = str(input("Password: "))
    print(user==usuarios.USUARIO and contra==usuarios.CONTRASEÑA)
data()