#Diseña un algortimo si una valor ingresado es una calificacion valida (0-20)

def notaValida(nota):
    if nota>=0 and nota<=20:
        return (f"El número {nota} cuenta como VÁLIDA.")
    else:
        return(f"El número {nota} cuenta como NO VÁLIDA")
print(notaValida(-1))
