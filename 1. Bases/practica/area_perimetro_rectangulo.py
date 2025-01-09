#Se solicita calcular el área y perímetro de un rectángulo aplicando las siguientes fórmulas:
#area = base*altura
#perimetro = 2*(base+altura)

def area(base,altura):
    area = base*altura
    return (f"Area: {(area)}")

def perimetro(base,altura):
    perimetro = (base+altura)*2
    return (f"Perímetro: {(perimetro)}")

def datos():
    base=int(input("Base: "))
    altura=int(input("Altura: "))
    print(area(base, altura))
    print(perimetro(base, altura))

datos()