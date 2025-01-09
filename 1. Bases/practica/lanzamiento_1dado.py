#Hacer una simulación de lanzamiento de 1 dado, que cuando salga el número 6 se vuelva a lanzar automáticamente (1 vez más como máximo)

from random import randint as rango
dado = rango(1,6)
dado2 = rango(1,6)

def throwAdditionalDice():
    return f"Tu lanzamiento adicional saca un: {dado2}"

def throwInitialDice():
    print(f"Lanzas el dado y sacas: {dado}")
    if dado==6:
        print(throwAdditionalDice())
    else:
        print("Terminó el lanzamiento.")

throwInitialDice()