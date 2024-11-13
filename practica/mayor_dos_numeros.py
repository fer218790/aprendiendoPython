#Crear un programa para indicar cual es el mayor de dos números
#EL programa debe pedir al usuario dos numeros enteros, para luego compararlos y mandar a imprimir el número mayor

def esMayor(a,b):
    if a!=b:
        dato = f"El mayor es: {a}" if a>b else f"El mayor es {b}"
    else:
        dato = ("Ambos números son iguales.")
    return dato

primer_numero = int(input("Ingresa el primer número: "))
segundo_numero = int(input("Ingresa el segundo número: "))
print(esMayor(primer_numero,segundo_numero))