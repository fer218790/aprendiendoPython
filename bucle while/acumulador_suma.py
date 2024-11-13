#Realizar la suma de los primeros 5 numeros usando un ciclo while
#1+2+3+4+5=15

acumulador = 0
contador=1
while contador<=5:
    acumulador=acumulador+contador
    contador+=1
print(acumulador)

#Otra manera:

MAXIMO = 5
suma = 0
inicio = 1
while inicio<=MAXIMO:
    suma += inicio
    inicio+=1
print(suma)
