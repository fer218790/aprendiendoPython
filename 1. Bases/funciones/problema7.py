def es_palindromo(palabra):
    palabra=palabra.replace(" ","") #borramos los espacios encontrados entre las palabras
    volteada = palabra[::-1] #volteamos la cadena usando el paso -1
    return volteada==palabra

resultado = es_palindromo("radar")
print(f"Es palíndromo? : {resultado}")
