lista = [1,2,3,4]
print(sum(lista))

lista1 = [1,2,3,4,5,6]

for numero in lista1:
    if numero%2==0:
        print(numero)
    else:
        print(f"El número {numero} es impar.")
else:
    print("Se acabó la iteración")


print("Generando una matriz identidad:")
matriz_identidad = [
    [1,0,0],
    [0,1,0],
    [0,0,1]]
print(matriz_identidad[0])
print(matriz_identidad[1])
print(matriz_identidad[2])
