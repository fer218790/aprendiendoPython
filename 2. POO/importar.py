import random
n=int(input("Ingrese el número de notas: "))

def Carga(n):
    notas = []
    for valor in range(n):
        valor = random.randint(12,20)
        notas.append(valor)
    notas.sort()
    return notas

print(f"Notas: {Carga(n)}")