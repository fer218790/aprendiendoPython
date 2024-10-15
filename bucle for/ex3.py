#Dada una cadena, escribe un programa que cuente cuántas letras hay en
#total (sin contar espacios).

cadena = str(input("Ingresa el texto pe causa: "))
letras = 0
espacios = 0
for i in cadena:
    if (i!=" "):
        letras+= 1
    else:
        espacios+=1
else:
    print(f"######\nEspacios encontrados: {espacios}")
    print(f"Letras en total: {letras}")
    
