#definir 2 funciones. una que calcule el perimetro y otra que calcule el área.
#perimetro = lado * 4
#area  = lado^2

def Area(a):
    area = a**2
    return area

def Perimetro(b):
    perimetro = b*4
    return perimetro

def Operacion():
    lado = float(input("Ingresa el lado del cuadrado: "))
    print(f"El área del cuadrado es: {Area(lado)}")
    print(f"El perímetro del cuadrado es: {Perimetro(lado)}")

Operacion()