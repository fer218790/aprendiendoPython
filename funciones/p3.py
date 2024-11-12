#Diseñar un algoritmo que determine si un número ingresado cualquier es par

def esPar(numero):
    if (numero%2==0):
        return (f"El número {numero} es par!")
    else:
        return(f"El número {numero} no es par :c")
print(esPar(16))