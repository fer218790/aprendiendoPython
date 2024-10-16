#v1.0: sumar minutos y segundos

total_minutos=0
total_segundos=0

while True:
    minutos = int(input("Ingresa minutos: "))
    if minutos>60:
        break
    segundos = int(input("Ingresa segundos: "))
    print(" ")#Para que haya un margen
    total_minutos+=minutos
    total_segundos+=segundos
print("##############################")
print(f"\nMinutos totales: {total_minutos} minutos")
print(f"Segundos totales: {total_segundos} segundos")

#v1.1: Calcular la cantidad de horas, minutos y segundos acumulados
