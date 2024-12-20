IGV = 0.18
PRECIO = 1
cantidad = (int(input("Ingresa la cantidad: ")))

subtotal = (PRECIO*cantidad)
print(f"Subtotal: {subtotal}")
print(f"Total: {subtotal+(IGV*subtotal)}")