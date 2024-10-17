####Ejercicio de Aplicación 1: Tuplas
####Crea una tupla con los siguientes valores: (10, 20, 30, 40, 50).
####Imprime el segundo valor de la tupla.
####Desempaqueta la tupla en 5 variables diferentes y muestra sus valores.
tupla = (10,20,30,40,50)
print(f"Segundo valor: {tupla[1]}")

diez, veinte, treinta, cuarenta, cincuenta = tupla
print(diez)
print(veinte)
print(treinta)
print(cuarenta)
print(cincuenta)


##Ejercicio de Aplicación 2: Diccionarios
##Crea un diccionario que contenga la siguiente información sobre una persona:
##Nombre: "Carlos"
##Edad: 30
##Profesión: "Ingeniero"
##País: "Colombia"
##Imprime el valor asociado con la clave "Nombre".
##Modifica la edad de la persona a 31.
##Agrega una nueva clave "Ciudad" con el valor "Bogotá".
##Imprime todas las claves y todos los valores del diccionario.

diccionario = {"nombre":"Carlos",
               "edad":30,
               "profesion":"ingeniero",
               "pais":"Colombia"}
print(diccionario["nombre"])
diccionario["edad"]=31
diccionario["ciudad"]="Bogotá"
print(f"Keys: {diccionario.keys()}")
print(f"Values: {diccionario.values()}")
print(f"Items: {diccionario.items()}")
