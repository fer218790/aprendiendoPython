##Ejercicio de Aplicación 4: Conjuntos con cadenas de texto
##Crea un conjunto llamado vocales que contenga las vocales: 'a', 'e', 'i', 'o', 'u'.
##Crea otro conjunto llamado letras_palabra que contenga las letras de la palabra "programacion".
##Realiza las siguientes operaciones y muestra los resultados:
##Intersección entre vocales y letras_palabra.
##Diferencia entre vocales y letras_palabra.

vocales = {"a","e","i","o","u"}
letras_palabra = {"p","r","o","g","r","a","m","a","c","i","o","n"}

interseccion = vocales & letras_palabra
diferencia = vocales - letras_palabra

print(f"Interseccion: {interseccion}")
print(f"Diferencia: {diferencia}")


##Ejercicio de Aplicación 5: Verificar subconjuntos
##Crea un conjunto conjunto_X = {1, 2, 3} y otro conjunto conjunto_Y = {1, 2, 3, 4, 5}.
##Verifica si conjunto_X es un subconjunto de conjunto_Y y muestra el resultado.
##Verifica si conjunto_Y es un superconjunto de conjunto_X y muestra el resultado.

con_x={1,2,3}
con_y={1,2,3,4,5}



if con_x.issubset(con_y):
    print("con_x es subconjunto de con_y")

if con_y.issuperset(con_x):
    print("con_y es superconjunto de con_x")
