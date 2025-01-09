def multiplicar(num1,num2):
    return num1*num2

resultado = multiplicar(4,5)
print(resultado)

print("-----------------------------------------")

def calcular_promedio(a,b,c):
    return (a+b+c)/3
resultado = calcular_promedio(6,8,10)
print(resultado)

print("-----------------------------------------")

x=10 #definiendo una variable globar con valor 10


def modificar_variable():
    global x
    x = 20
    print(f"Valor de x dentro de la función: {x}")

print(f"Antes: {x}")
modificar_variable()
print(f"Ahora: {x}")

print("-----------------------------------------")

def es_par(numero):
    return numero%2==0

print(f"El número 7 es par?: {es_par(7)}")
