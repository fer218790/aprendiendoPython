#Escribe un programa que sume solo los números impares del 1 al 100 e
#imprima el resultado.

cantidad_impares=0
for i in range(1,101):
    if (i%2!=0):
        cantidad_impares+=i
else:
    print(f"Suma impares: {cantidad_impares}")
