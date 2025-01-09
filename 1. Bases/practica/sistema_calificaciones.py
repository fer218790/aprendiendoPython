#Crear un programa para convertir una calificacion numérica (entre 0 y 20) a una letra (AD, A, B y C)
#Rangos de calificaciones
#0-7: C
#8-13: B
#14-16: A
#17-20: AD

C=(0,1,2,3,4,5,6,7)
B=(8,9,10,11,12,13)
A=(14,15,16)
AD=(17,18,19,20)

def rangoNotas(a):
    if a in C:
        return f"Sacaste C"
    elif a in B:
        return f"Sacaste B"
    elif a in A:
        return f"Sacaste A"
    elif a in AD:
        return f"Sacaste AD"
    else:
        return f"Taz kinseao"

def intro():
    dato = int(input("Ingresa tu nota (0-20): "))
    if dato in range(0,21):
        print(rangoNotas(dato))
    else:
        print(intro())

intro()