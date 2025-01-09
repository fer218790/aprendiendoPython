#Usando el operador not para aplicar logica inversa, se debe hacer un programa con las siguientes condiciones:

#Si NO deseamos salir del sistema, imprimir:
    #Continuamos dentro del sistema
#De lo contrario:
    #Saliendo del sistema

def mensaje(respuesta):
    if not respuesta:
        return "Continuamos dentro del sistema"
    else:
        return "Saliendo..."

pregunta = input("Deseas salir del sistema? (SI/NO): ")
pregunta = pregunta.upper() == 'SI'
print(mensaje(pregunta))