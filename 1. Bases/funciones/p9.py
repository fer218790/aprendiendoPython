#Ingresa un numero y calcular la suma de naturales hasta ese numero

def sumaNaturales(numero):
    suma=0
    for i in range(numero+1):
        suma=i+suma
    else:
        return (f"La suma de naturales hasta {numero} es: {suma}")

print(sumaNaturales(10))