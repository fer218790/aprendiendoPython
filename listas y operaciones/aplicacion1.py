###Operaciones básicas con listas
##1. Crea una lista con los números del 1 al 5.
##2. Accede e imprime el tercer elemento.
##3. Modifica el segundo elemento para que sea 20.
##4. Agrega el número 6 al final de la lista.
##5. Inserta el número 0 al inicio de la lista.
##6. Elimina el tercer elemento de la lista.
##7. Imprime la lista resultante.

#1
lista = [1,2,3,4,5]

#2
print(lista[2])

#3
lista[1] = 20
print(lista)

#4
lista.append(6)

#5
lista.insert(0,0)

#6
lista.pop(2)

#7
print(lista)
print("#########################")

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista[2:6])
print("#########################")
lista = [5,2,9,1,5,6]
lista.sort()
print(lista)
lista.reverse()
print(lista)
