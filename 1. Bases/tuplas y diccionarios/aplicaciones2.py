##Ejercicio de Aplicación 3: Operaciones con Tuplas
##Crea una tupla con los números del 1 al 10.
##Extrae una subtupla con los primeros 5 elementos de la tupla original.
##Imprime la tupla original y la subtupla.

tupla = (1,2,3,4,5,6,7,8,9,10)
subtupla = tupla[0:5]
print(f"Tupla: {(tupla)}")
print(f"Subtupla: {(subtupla)}")

##Ejercicio de Aplicación 4: Modificación de Diccionarios
##Crea un diccionario que represente un carrito de compras con los siguientes artículos y sus precios:
##
##Manzanas: 1.20
##Plátanos: 0.80
##Leche: 2.50
##Agrega un nuevo artículo llamado "Pan" con un precio de 1.50.
##
##Elimina el artículo "Plátanos" del diccionario.
##
##Imprime el diccionario actualizado.

carrito = {
    "manzanas":1.20,
    "platanos":0.80,
    "leche":2.50
    }
carrito["pan"]=1.50
print(f"Alimentos en el carrito: {(carrito)}")

del carrito["platanos"]
print(f"Alimentos actualizados en el carrito: {(carrito)}")

##Ejercicio de Aplicación 5: Combinar Listas y Diccionarios
##Crea una lista llamada personas que contenga tres diccionarios. Cada diccionario debe representar una persona y tener las claves: "Nombre", "Edad" y "Ciudad".
##
##La primera persona es "Juan", 25 años, de "Lima".
##La segunda persona es "María", 30 años, de "Bogotá".
##La tercera persona es "Pedro", 22 años, de "Quito".
##Recorre la lista e imprime el nombre de cada persona seguido de su ciudad.

personas = [{"nombre":"Juan","edad":25,"ciudad":"Lima"},
            {"nombre":"María","edad":30,"ciudad":"Bogotá"},
            {"nombre":"Pedro","edad":22,"ciudad":"Quito"}]

for i in personas: #Recorre los elementos y busca la key en cada diccionario
    #print(i)
    print(f"Nombre: {i["nombre"]}, Ciudad: {i["ciudad"]}")




















