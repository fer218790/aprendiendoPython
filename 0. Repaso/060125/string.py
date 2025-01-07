def separador():
    print("********************************************************************************")

miPal = "hello world darling!"
#print(dir(miPal))
#convirtiendo cadena a CAPS
miPal = miPal.upper()
print(f"Cadena convertida a mayúscula: {miPal}")
miPal = miPal.swapcase()
print(f"Usando el método swapcase para cambiar entre mayusculas y minúsculas: {miPal}")
miPal = miPal.replace("darling","kerida xd")
print(f"Cambiar el \"darling\" por \"kerida xd\": {miPal}")

#Contar la cantidad de letras en un string
miPal = "world hello darling!"
print(f"Cantidad de letras \"l\" en la cadena \"{miPal}\": {miPal.count("l")} letras.")
print(f"¿Empieza con hello?: {miPal.startswith("hello")}")
print(f"¿Terminan con !?: {miPal.endswith("!")}")
#Usa el argumento indicado para separar las palabras. lo guarda en una lista.
print(miPal.split("o"))

#Busca el valor indicado y devuelve el índice
miPal = "Esternocleidomastoideo"
print(miPal.find("r"))

#Mostrar la longitud de la palabra:
print(len(miPal))
#Buscar el indice de lo que indicamos
print(miPal.index("ster"))
#Saber si mi variable es numérica
print(miPal.isnumeric())
separador()

#Realice un algoritmo para elaborar la suma de los N primeros números consecutivos
n = 5
suma = (n*(n+1))/2
print(f"Suma de N primeros números consecutivos: {suma}")
separador()
#Realice el algoritmo que de entrada tenga notas y nombres de 5 alumnos y a la salida te muestre si aprobaron o no.
