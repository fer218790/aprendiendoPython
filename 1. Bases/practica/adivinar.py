#Crear un juego donde el jugador debe adivinar un número secreto (del 10 al 20)
#Por cada intento fallido se debe contar y al finalizar mostrar cuantos intentos fallidos hubieron.

from random import randint as adivina
door = False
NUMERO = adivina(10,20)
print("Numero aleatorio generado: **.")
contador=0
while not door:
    usuario = int(input("Ingresa un número del 10 al 20: "))
    if NUMERO==usuario:
        print(f"Tu número {usuario} acertó con el número generado aleatoriamente!\n")
        door = True
    else:
        print(f"No le acertaste :c. Inténtalo nuevamente.\n")
        contador+=1
print(f"Intentos fallidos hasta que le atinaste: {contador}")