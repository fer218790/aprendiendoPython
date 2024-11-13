
door = False
saldo = 1000
while not door:
    print(''' Menu:
    1. Ver saldo
    2. Retirar dinero
    3. Depositar dinero
    4. Salir del sistema''')
    option = int(input("Selecciona una opción: >> "))
    
    if option==1:
        print(f"Tu saldo es de: {saldo}\n")
    elif option==2:
        retiro = float(input("Cuánto quieres retirar?: >> "))
        saldo = saldo-retiro
        print(f"Has retirado S/ {retiro}. Te quedan S/{saldo}.")
    elif option==3:
        deposito = float(input("Cuánto quieres depositar?: >> "))
        saldo+=deposito
        print(f"Has depositado S/ {deposito}. Cuentas con {saldo}")
    elif option==4:
        door = True
        print("Hasta luego! \n")
    else:
        print("Opción inválida. Elige otra opción")