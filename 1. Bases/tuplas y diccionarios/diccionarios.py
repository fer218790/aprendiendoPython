diccionario = {
    "Nombre": "Juan",
    "Edad": 25,
    "Ciudad": "Lima"
    }
print(diccionario)
print("#######################################################")
print(f"El nombre almacenado en el diccionario es: {diccionario["Nombre"]}")
print(f"La edad almacenada en el diccionario es: {diccionario["Edad"]}")
print(f"Donde vive? En {diccionario["Ciudad"]}")
print("#######################################################")

#Modificar un value asociada a una key:
    #Cambiaremos los values de las keys por mis datos actuales
print(f"""Diccionario inicial:
    Nombre inicial: {diccionario["Nombre"]}
    Edad inicial: {diccionario["Edad"]}
    Ciudad inicial: {diccionario["Ciudad"]}""")

diccionario["Nombre"]=str(input("Ingresa tu nuevo nombre: "))
diccionario["Edad"]=int(input("Tu nueva edad: "))
diccionario["Ciudad"]=str(input("Ciudad nueva: "))
print(f"""\nDiccionario actualizado:
    Nombre actualizado: {diccionario["Nombre"]}
    Edad actualizada: {diccionario["Edad"]}
    Ciudad actualizada: {diccionario["Ciudad"]}""")

#Agregando nuevos key-value:
diccionario["Pais"]=str(input("Ingresa el país: "))
print(diccionario)

#Borrar un par key-value
del diccionario["Pais"]
print(diccionario)

#Métodos útiles en diccionarios:
    #keys(): Devuelve la lista de todas las keys
    #values(): Deuvelve la lista de todos los values
    #items(): Deuvelve la lista de pares key-value

print(f"Método keys(): Muestra todas las keys del diccionario. {diccionario.keys()})")
print(f"Método values(): Muestra todos los values. {diccionario.values()}")
print(diccionario.items())
