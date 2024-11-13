#Meses 1,2 o 12 -> Invierno
#Meses 3,4 o 5 -> Primavera
#Meses 6,7 u 8 -> Verano
#Meses 9, 10 u 11 -> Otoño
#Cualquier otro valor -> Unkown Stage

INVIERNO = (1,2,12)
SPRING = (3,4,5)
SUMMER = (6,7,8)
AUTUNM = (9,10,11)
def estacion(a):
        if a in INVIERNO:
            return "Winter falls"
        elif a in SPRING:
            return "Spring falls"
        elif a in SUMMER:
            return "Summer falls"
        elif a in AUTUNM:
            return "Autunm falls"
        else:
            return "Uknown Stage"
dato = int(input("Dame un número de estación (1 al 12): "))
print(estacion(dato))