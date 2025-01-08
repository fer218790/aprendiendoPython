#Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación, imprimir "coincidencia" si los nombres de ambas personas comienzan con la misma letra o si terminan con la misma letra. Si no es así, imprimir "no hay coincidencia"

nombre1 = str(input("Ingresa el name 1: "))
nombre2 = str(input("Ingresa el name 2: "))

if (nombre1[0] == nombre2[0]) or (nombre1[-1] == nombre2[-1]):
    print("Coincidencia")
else:
    print("No hay coincidencia")

#Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son:
#candidato A por el partido rojo
#candidato B por el partido verde
#candidato C por el partido azul
#Segun el candidado elegido, se le debe imprimir un mensaje "Usted ha votado por el partido [color que corresponde]". Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar "opción erronea"

candidatos_y_partidos = {'A':'Partido rojo', 'B':'Partido verde','C':'Partido azul'}
opcion = str(input("Elige tu candidato (A, B o C):\n>> "))
opcion = opcion.upper()
if opcion in candidatos_y_partidos:
    print(f"Usted ha votado por el partido {candidatos_y_partidos.get(opcion)}")
else:
    print("Opción errónea")