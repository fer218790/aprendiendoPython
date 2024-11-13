#Se solicita crear una aplicacion de salud y fitness que solicite lo siguiente:
#Nombre de usuario
#Pasos caminados en el día
#Además, definiremos las siguientes constantes:
#META_PASOS_DIARIO = 10000
#CALORIAS_POR_PASO = 0.04
#Con los valores anteriores, debemos calcular las calorias quemadas segun los pasos caminados
#calorias_quedamas = pasos_diarios * CALORIAS_POR_PASO
#Y verificamos si se cumplió la meta de pasos diarios 
#meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS -> Se alcanzó la meta/No se alcanzó la meta

META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04

def meta(nombre,pasos):
    #nombre = input("Nombre: ")
    #pasos = int(input("Cantidad de pasos: "))
    calorias_quedamas = pasos * CALORIAS_POR_PASO
    meta_alcanzada = f"{nombre}, usted SÍ alcanzó la meta." if (pasos >= META_PASOS_DIARIO) else "usted NO alcanzó la meta."
    print(meta_alcanzada)

def datos():
    nombre = input("Nombre: ")
    pasos = int(input("Cantidad de pasos: "))
    meta(nombre,pasos)

datos()

