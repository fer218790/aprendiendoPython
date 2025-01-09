##Ejercicio de Aplicación 1: Crear y manipular conjuntos
##Crea un conjunto llamado conjunto_numeros con los números 1, 2, 3, 4, 5.
##Añade el número 6 al conjunto.
##Elimina el número 3 del conjunto.
##Verifica si el número 4 está en el conjunto e imprime el resultado.

conjunto_numeros = {1,2,3,4,5}
print(f"Conjunto inicial: {conjunto_numeros}")

conjunto_numeros.add(6)
print(f"Añadiendo el número 6 al conjunto: {conjunto_numeros}")

    #conjunto_numeros.remove(7) #Genera un error si el item no está en el set
conjunto_numeros.discard(3) #No genera un error si el item no está en el set

print(f"Elemento \'3\' eliminado. Nuevo conjunto: {conjunto_numeros}")

if 4 in conjunto_numeros:
    print("Está en el set")
else:
    print("No está en el set")

##Ejercicio de Aplicación 2: Operaciones entre conjuntos
##Crea dos conjuntos:
##
##conjunto_A = {1, 2, 3, 4}
##conjunto_B = {3, 4, 5, 6}
##Realiza las siguientes operaciones y muestra los resultados:
##
##Unión de conjunto_A y conjunto_B.
##Intersección de conjunto_A y conjunto_B.
##Diferencia entre conjunto_A y conjunto_B (elementos en conjunto_A que no están en conjunto_B).

conA={1,2,3,4}
conB={3,4,5,6}

print(f"Union: {(conA|conB)}")#union
print(f"Interseeción: {conA&conB}")#interseccion
print(f"Diferencia: {conA-conB}")#diferencia


##Ejercicio de Aplicación 3: Conversión de lista a conjunto
##Crea una lista con los siguientes elementos (algunos repetidos): [1, 2, 2, 3, 4, 4, 5, 5, 5].
##Convierte la lista a un conjunto para eliminar duplicados.
##Muestra el conjunto resultante.
lista = [1,2,2,3,4,4,5,5,5]
lista = set(lista)
print(lista)
