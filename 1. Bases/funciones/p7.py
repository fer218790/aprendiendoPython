#determina si un numero es positivo o negativo

def posiOnega(numero):
    if numero>0:
        print("Positivo")
    else:
        if numero<0:
            print("Negativo")
        else:
            print("Es cero")
posiOnega(-10)

def otraManera(dato):
    if dato>0:
        print("Es positivo")
    elif dato<0:
        print("Es Negativo")
    else:
        print("Es cero")
otraManera(-0)