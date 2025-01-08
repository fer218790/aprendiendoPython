#Funciones: Son bloques de algoritmos que realizan un algoritmo en específico
def Factorial(n):#parámetro
    count=1
    if n>0:
        while n>0:
            count=count*n
            n=n-1
    return count
Fac = Factorial(3)
n=int(input("Ingresa el número: "))
print(f"El factorial de {n} es: {Fac}")