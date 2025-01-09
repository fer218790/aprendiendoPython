conjunto = {1,2,3,4,5,6,7,8,9,10,1}
print(conjunto)

#agregando un elemento al conjunto
conjunto.add(11)
print(conjunto)

conjunto.remove(1)
print(conjunto)

conjunto.add(1)
print(conjunto)

numero = int(input("Ingresa el número para ver si está: "))
if numero in conjunto:
    print("Está!")
else:
    print("Nel perro")

#operaciones entre conjuntos:
    #unión: Une los elementos de los conjuntos

a = {1,2,3}
b = {3,4,5}
union = a|b
print(union)

    #intersección: Muestra los elementos que están en ambos conjuntos
interseccion = a&b
print(interseccion)

    #diferencia: 
diferencia = b-a
print(diferencia)

lista = [1,2,3,4,5,6,6,7,8]
print(type(lista))
lista = set(lista)
print(type(lista))
print(lista)
