##matriz = [
##    [1,2,3],
##    [4,5,6],
##    [7,8,9]
##    ]
##
##fila_a = sum(matriz[0])
##fila_b = sum(matriz[1])
##fila_c = sum(matriz[2])
##
##columna_a = matriz[0][0]+matriz[1][0]+matriz[2][0]
##columna_b = matriz[0][1]+matriz[1][1]+matriz[2][1]
##columna_c = matriz[0][2]+matriz[1][2]+matriz[2][2]
##print(f"Suma de filas: [{fila_a},{fila_b},{fila_c}]")
##print(f"Suma de columnas: [{columna_a},{columna_b},{columna_c}]")


matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

suma_filas = []
suma_columnas=[0]*len(matriz)

for fila in matriz:
    suma_filas.append(sum(fila))

for i in range(len(matriz)): #recorre fila
    for j in range(len(matriz[i])): #recorre columna
        suma_columnas[j]= suma_columnas[j]+matriz[i][j]

print(f"Suma de filas: {suma_filas}")
print(f"Suma de columnas: {suma_columnas}")
