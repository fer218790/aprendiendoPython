#numero = int(input("Numero: "))


def calc_factorial(numero):
    factorial = 1
    for i in range(1,numero+1):
        factorial = factorial*i
        #print(factorial)
    return factorial

resultado = calc_factorial(5)
print(f"Factorial de 5: {resultado}")
