#Funciones: Son bloques de algoritmos que realizan un algoritmo en específico
def Factorial(n):#parámetro
    count=1
    if n>0:
        while n>0:
            count=count*n
            n=n-1
    return count

def Combinatoria(a,b):
    num = Factorial(a)
    den = Factorial(a-b)*Factorial(b)
    comb = num/den
    return comb

x = int(input("Ingresa el número de elementos: "))
y = int(input("En cuántos grupos desea agrupar?: "))
print(f"El número de grupos es: {int(Combinatoria(x,y))}")