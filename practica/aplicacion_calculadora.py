#Hacer un menu principal que muestre las 4 operaciones básicas, luego ingresar datos por teclado y que haga la operación solicitada
door = False


while not door:
    print("""Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir""")
    opcion = int(input("Escoge una opción: >> "))
    
    if opcion in range(1,5):
        a=int(input("Ingresa el primer numero: "))
        b=int(input("Ingresa el segundo numero: "))

    if opcion==1:
        print(f"El resultado de la suma es: {a+b}")
    elif opcion==2:
        print(f"El resultado de la resta es: {a-b}")
    elif opcion==3:
        print(f"El producto es: {a*b}")
    elif opcion==4:
        print(f"El cociente es: {a/b}")
    elif opcion==5:
        print("Nos fuimo!")
        door = True
    else:
        print("Te has kinseao")