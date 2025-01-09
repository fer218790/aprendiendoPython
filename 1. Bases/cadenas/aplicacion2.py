##Ejercicio de Aplicación 4: Repetición de cadenas y formateo
##Crea una cadena llamada frase con el valor "Python es genial!".
##Repite la cadena 3 veces y almacena el resultado en frase_repetida.
##Usa f-strings para crear una cadena que diga: "La frase repetida es: [frase_repetida]".
##Imprime el resultado.
##

##cadena = "Python es awesome!"
##frase_repetida = cadena*3
##print(f"La frase repetida es: {frase_repetida}")

##Ejercicio de Aplicación 5: Reemplazo y conteo de caracteres
##Crea una cadena llamada mensaje con el valor "Python es un lenguaje de programación muy popular".
##Reemplaza la palabra "Python" por "JavaScript".
##Cuenta cuántas veces aparece la letra "a" en la cadena y muestra el resultado.

message = "Python es un lenguaje de programación muy popular"
message=message.replace("Python","JavaScript")
print(message)

message=message.count('a') #Usamos el método count() para contar!
print(f"Veces que se repite la letra A: {message}")
