#Crear un menu que permita crear y eliminar cuenta; así como también la opción de salir

door = False

while not door:
    print(''' Menu:
    1. Sign up
    2. Delete your account
    3. Log out''')
    option = int(input("Select an option: >> "))

    if option==1:
        print("Creating your account... \n")
    elif option==2:
        print("Deleting your account... \n")
    elif option==3:
        print("Logging outta system. See you around!")
        door = True
    else:
        print("Invalid option. Please, select a valid option. \n")