mi_lista = [1,2,3,4,5]
print(mi_lista[0]) #Imprime el primer elemento
print(mi_lista[4]) #Imprime el último elemento

#Asignando un valor en el índice correspondiente
mi_lista[2] = 10 #Cambia el número 3 por el 10
print(mi_lista)
#Longitud de una lista
print(f"Longitud de la lista: {len(mi_lista)} elementos.")

#Agregamos elementos
    #Existen dos formas:
    #1. append(): Añade elemento al final de la lista
    #2. insert(): Inserta el elemento en un índice específico
mi_lista.append(6)
print(f"\nHemos agregado un elemento con append: {mi_lista}")
mi_lista.insert(2,3)
print(f"\nHemos insertado el valor de 10 en el índice 2: {mi_lista}")

#Eliminamos elementos
    #Existen dos formas:
    #1. remove(): Elimina por valor
    #2. pop(): Elimina por índice (último índice por defecto)
mi_lista.remove(10)
mi_lista.pop(3)
print(mi_lista)


