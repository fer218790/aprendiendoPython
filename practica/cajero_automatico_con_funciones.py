#Hacer un cajero automático que permita depositar, retirar y consultar el saldo
#saldo inicial = 1000 soles
#Si al final del viaje terminarás enterrado, de qué sirve vivir la vida estando tan preocupado?

print("*** Main Menu ***")

def menuPrincipal():
    print("""Select an option:
        1. Consulta de saldo
        2. Retiro de dinero
        3. Depósito de dinero
        4. Terminar sesión """)
    opcion = int(input(">> "))
    controlador(opcion)

def controlador(opcion):
    if opcion==1:
        consultaSaldo()
    elif opcion==2:
        retiroDinero()
    elif opcion==3:
        depositoDinero()
    elif opcion==4:
        print("Sesión finalizada. Retire su tarjeta.")
    else:
        print("Opción inválida. Seleccione una opción válida.")
        menuPrincipal()

def consultaSaldo():
    saldo = 1000
    print(f"Usted tiene un saldo de: {saldo}")
    pass

def retiroDinero():
    retiro = float(input("Cuánto desea retirar?: "))
    

    pass

def depositoDinero():
    pass

menuPrincipal()