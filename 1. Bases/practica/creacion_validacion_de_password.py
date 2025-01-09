#Crear un programa que solicite la validación de crear una contraseña
#La contraseña debe tener al menos 6 caracteres.
#Si no sucede, entonces debe volver a solicitar un nuevo valor hasta que cumpla con la condicion
#Si es valido debe imprimir "Contraseña válida" y terminar la ejecución


door = False
while not door:
    contra = input("Ingresa la contraseña: ")
    if len(contra)<6:
        print("Longitud de la contraseña inválida. Inténtalo nuevamente.\n")
    else:
        print("Contraseña segura creada satisfactoriamente!\n")
        door = True