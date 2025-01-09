#Crea un programa para determinar el costo de envio de un paquete según el destino (nacional o internacional) y el peso del paquete.

#Tarifario:
#Nacional -> 10 x kilo
#internacional -> 20 x kilo
#El programa debe solicitar 2 valores:
    # Destino (nacional o internacional)
    # Peso (kg) del paquete
#Al final se debe imprimir el costo de envío del paquete

NACIONAL = 10
INTERNACIONAL = 20

def calcularCosto(destino,peso):
    if destino == 'N':
        print(f"Destino Nacional. Costo total: {peso*NACIONAL}")
    else:
        print(f"Destino Internacional. Costo total: {peso*INTERNACIONAL}")

def main():
    DESTINO = ("I","N")
    dato = input("Nacional o Internacional? (N/I)")
    dato = dato.upper()
    peso = float(input("Peso: "))
    if dato not in DESTINO:
        return main()
    else:
        calcularCosto(dato,peso)
    
main()