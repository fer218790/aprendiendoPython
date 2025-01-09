#Se solicita crear un sistema de reservación de un hotel.
#Nombre del cliente
#Dias de estadia en el hotel
#Cuarto con vista al mar?
#Tarifario:
#Cuarto sin vista al mar: 150.50 soles por día
#Cuarto con vista al mar: 190.50 soles por dia

#El sistema debe calcular el costo total de la estadia dependiendo si escogió un cuarto con vista al mar o no, además de indicar si se escogió un cuarto con vista al mar o no
CON_VISTA=190.5
SIN_VISTA=150.5

def datos():
    nombre_cliente=input("Nombre del cliente: ")
    dias_estadia = int(input("Cantidad de días: "))
    vista = input("Con vista al mar? (S/N): ")
    vista = vista.upper()=='S'
    print(calcular(nombre_cliente,dias_estadia,vista))

def calcular(cliente,dias,vista):
    total = f"Sr(a) {cliente}, su total a pagar es: {dias*SIN_VISTA}" if not vista else f"Sr(a) {cliente}, su total a pagar es: {dias*CON_VISTA}"
    return total

datos()