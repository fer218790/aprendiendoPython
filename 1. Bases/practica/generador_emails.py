#Crear un generador de emails
#Nombres -> Luis Fernando
#Apellidos -> Donayre Quispe
#Nombre Empresa -> Flow State
#extensión dominio -> .pe

nombres = input("Ingresa tus nombres: ")
apellidos = input("Ingresa tus apellidos: ")
empresa = input("Ingresa nombre de empresa: ")
extension = input("Dominio: ")

nombres = nombres.lower()
nombres = nombres.replace(" ",".")

apellidos = apellidos.lower()
apellidos = apellidos.replace(" ",".")

empresa = empresa.lower()
empresa = empresa.replace(" ","")
print(f"Tu nuevo correo es: {nombres}.{apellidos}@{empresa}{extension}")
