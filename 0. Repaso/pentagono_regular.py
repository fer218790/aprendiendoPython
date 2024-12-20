q = int(input("Ingresa el número de lados: "))
medida_q = float(input("Ingresa la medida del lado: "))
apotema = float(input("Ingresa la medida de la apotema: "))

PERIMETRO = q*medida_q
AREA = apotema*PERIMETRO

print(f"""Perímetro: {PERIMETRO}
Área: {AREA} """)