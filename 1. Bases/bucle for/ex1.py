#Escribe un programa que sume todos los números del 1 al 100 e imprima
#el resultado

suma=0
for i in range(101):
    print(f"Valor de i: {i}")
    suma=suma+i
    print(f"Suma hasta {i}: {suma}\n")
else:
    print(f"Suma total: {suma}")

print("Ya terminé")
