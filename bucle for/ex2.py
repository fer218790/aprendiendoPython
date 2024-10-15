#EEscribe un programa que imprima solo los números pares del 1 al 50.

suma = 0

for i in range(1,51):
    if (i%2==0):
        print(f"Número par: {i}")
else:
    print("No hay más valores para evaluar")
