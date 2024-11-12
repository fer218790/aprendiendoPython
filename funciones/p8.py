#Calcular el promedio de N números ingresados

def promedioNumeros(veces):
    suma=0
    for i in range(1,veces+1):
        numero = int(input("Ingresa el número: "))
        suma = suma+numero
    else:
        print(f"El promedio de {veces} numeros es: {int(suma/veces)}")

promedioNumeros(3)