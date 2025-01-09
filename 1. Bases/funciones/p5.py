#determina si un numero ignresado cualquiera es de 1 digito

def unDigito(numero):
    if (numero>-10 and numero<10):
        return(f"El numero {numero} es de 1 dígito")
    else:
        return(f"El numero {numero} no es de 1 digito")

print(unDigito(0))