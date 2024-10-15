#Escribe un programa que cuente cuántas vocales (a, e, i, o, u) hay en
#una cadena dada.

vocales="aeiou"
cadena = str(input("Ingresa la cadena: "))
cantidad_vocales=0

for i in cadena:
    if i in vocales:
        cantidad_vocales += 1
else:
    print(f"Cantidad de vocales: {cantidad_vocales}")
