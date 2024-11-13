#crear un sistema que ofrezca descuentos dependiendo del monto de la compra o si es miembro de la tienda

#Se deben revisar las siguientes condiciones:
#1. Si ha comprado más de S/1000 y es miembro -> Descuento de 10%
#2. Si solo es miembro de la tienda -> Descuento del 5%
#3. Si no es miembro ni compró más de S/ 1000 -> Sin descuento

MONTO_COMPRA_DESCUENTO = 1000

monto = int(input("Monto de compra: "))
miembro = str(input("Miembro? (S/N): "))

desc=0
#descontado = monto*desc

#mensaje_descuento = (f"""
#        Felicidades! Has obtenido un descuento del {desc*100}%
#        Monto de la compra: S/ {monto}
#        Cantidad descontada: S/ {descontado}
#        Monto a pagar: S/ {monto-descontado}""")

#mensaje = print(f"Monto a pagar: S/ {monto}")
#1. Si ha comprado más de S/1000 y es miembro -> Descuento de 10%
if (monto>=MONTO_COMPRA_DESCUENTO and miembro=='S'):
    desc=0.1
    descontado = monto*desc
    mensaje_descuento = (f"""
        Felicidades! Has obtenido un descuento del {desc*100}%
        Monto de la compra: S/ {monto}
        Cantidad descontada: S/ {descontado}
        Monto a pagar: S/ {monto-descontado}""")
    print(mensaje_descuento)

#2. Si solo es miembro de la tienda -> Descuento del 5%
elif (monto<MONTO_COMPRA_DESCUENTO and miembro=='S'):
    desc=0.05
    descontado = monto*desc
    mensaje_descuento = (f"""
        Felicidades! Has obtenido un descuento del {desc*100}%
        Monto de la compra: S/ {monto}
        Cantidad descontada: S/ {descontado}
        Monto a pagar: S/ {monto-descontado}""")
    print(mensaje_descuento)

#3. Si no es miembro ni compró más de S/ 1000 -> Sin descuento
elif (monto<MONTO_COMPRA_DESCUENTO and miembro=='N'):
    mensaje = print(f"Monto a pagar: S/ {monto}")
    print(mensaje)