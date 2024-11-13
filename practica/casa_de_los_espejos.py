#Suponemos que estoy en un parque de diversiones y quieres entrar a la casa de los espejos
#Sin embargo, debes cumplir con algunas condiciones:
#1. Debes tener más de 10 años
#2. No debe darte miedo la oscuridad
#Si se cumplen las condiciones anteriores puedes entrar
#Para realizar este ejemplo vamos a usar el operador not para aplicar una lógica inversa

edad = str(input("Mayor de 10 años? (S/N): "))
edad = edad.upper() == 'S'
miedo = str(input("Miedo a la oscuridad? (S/N): "))
miedo = miedo.upper() == 'S'

if not (edad and not miedo):
    print("No puedes entrar!")

#if not miedo and edad>=10:
#    print("Puedes entrar!")
#else:
#    print("No manito, ve a descansar")