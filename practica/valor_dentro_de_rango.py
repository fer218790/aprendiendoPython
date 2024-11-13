#Solicitar al usuario un valor entre 0 y 5 e indicarle si el valor proporcionado está dentro del rango
#Definir 2 constantes:
# VALOR_MINIMO = 0 y VALOR_MÁXIMO = 5
#Comprobar si el valor proporcionado se encuentra en el rango entre 0 y 5
#Se debe imprimir: Valor dentro de rango: True/False

VALOR_MINIMO = 0 
VALOR_MAXIMO = 5

def definir(parametro): #
    print(parametro in range(VALOR_MINIMO,VALOR_MAXIMO+1)) #Se hace una comprobación si el valor "parametro" está en el range de las constantes. Devuelve el valor de True o False, segun corresponda.

argumento = int(input("Ingresa el valor: "))    #Se pregunta al usuario y se almacena en la variable valor
definir(argumento)                              #Se pasa valor por la variable argumento