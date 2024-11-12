#Diseñar un algoritmo que determine si un número ingresado pertenece a la edad de un niño o un anciano
#niño entre 0 y 12 años
#anciano entre 60 y 100 años
def ninoViejo(edad):
    if (edad>=0 and edad<=12):
        return f"Edad: {edad} .: Es niño"
    elif (edad>=60 and edad<=100):
        return f"Edad: {edad} :. Es anciano"
    else:
        return "Edad no válida"
print(ninoViejo(35))