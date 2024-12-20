#Un codigo que calcule el perímetro y área de un círculo dado su radio
from math import pi
radio = float(input("Ingresa el radio: "))
perimetro = 2*pi*radio
area = pi*(radio**2)
print(f"Perímetro: {perimetro}")
print(f"Área: {area}")