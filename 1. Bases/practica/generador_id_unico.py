#Sistema Generador ID único
#Pide nombre, apellido y año
#1. Del valor de nombre, usar solo las 2 primeras letras y convertirlas a mayúsculas
#2. Del valor de apellido, usar las 2 primeras letras y convertirlas a mayúsculas
#3. Del valor de año, tomar los 2 últimos dígitos
#Además, el sistema debe generar un valor aleatorio de 4 dígitos, con ayuda de la función randint

#Formato de ID único:
# JUPE957326
from random import randint

def generador_id_unico(nombre,apellido,anio):
    no = (nombre[0:2]).upper()
    ap = (apellido[0:2]).upper()
    io = anio[2:]
    valor = randint(1000,10000)
    id=(f"{no}{ap}{io}{valor}")
    print(f"""\nHola {nombre.capitalize()},
    Tu ID generado es: {id}
    Felicidades!""")


#def datos():
#    nombre = str(input("Cuál es tu nombre? "))
#    apellido = str(input("Cuál es tu apellido? "))
#    anio = str(input("Cuál es tu año de nacimiento (AAAA)? "))
#    generador_id_unico()


generador_id_unico("Fernando","Donayre","1995")

