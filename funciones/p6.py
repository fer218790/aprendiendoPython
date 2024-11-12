#determina si un numero ingresado es de 3 digitos
def treDigitos(numero):
    if (numero>99 and numero<1000):
        return "Es de 3 digitos"
    else:
        return "No es de 3 digitos"
    
print(treDigitos(1000))