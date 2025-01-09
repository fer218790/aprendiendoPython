##Ejercicio de Aplicación 1: Operaciones básicas con cadenas
##Crea una cadena llamada saludo con el valor "Hola, Mundo!".
##Convierte la cadena a minúsculas y almacena el resultado en saludo_minuscula.
##Crea una nueva cadena que sea la concatenación de saludo_minuscula con la cadena " Esto es Python!".
##Imprime la longitud de la nueva cadena.


saludo = "Hola, Mundo!"
saludo_minuscula = saludo.lower()
print(saludo_minuscula+" Esto es Python")

##Ejercicio de Aplicación 2: Acceso a caracteres y slicing
##Crea una cadena llamada palabra con el valor "Programación".
##Accede al primer y último carácter de la cadena.
##Extrae una subcadena con los primeros 5 caracteres.
##Imprime la subcadena.

cadena = "Programación"
print(f"""Primer caracter: {cadena[0]}
Segundo caracter: {cadena[-1]}""")

subcadena = cadena[0:5]
print(subcadena)

##Ejercicio de Aplicación 3: Métodos de cadena
##Crea una cadena llamada frase con el valor " Aprende Python desde cero ".
##Elimina los espacios en blanco al inicio y al final de la cadena.
##Divide la cadena en una lista de palabras.
##Reemplaza la palabra "Python" por "programación" y muestra el resultado.

frase = (" Aprende Python desde cero ")
frase = frase.strip()
print(frase)
frase = frase.replace("Python","programación")
print(frase)
