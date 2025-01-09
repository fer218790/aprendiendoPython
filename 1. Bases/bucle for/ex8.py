#Dada una lista, escribe un programa que imprima todos sus elementos en
#orden inverso.

lista = [1,2,3,4,5,6]
#lista.reverse()
#print(lista)
#lista.reverse()
#print(len(lista))


for i in range(len(lista)-1,-1,-1):
    print(lista[i])
