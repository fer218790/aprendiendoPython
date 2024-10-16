#BREAK

contador = 1
while contador <= 10:
    if contador == 6:
        break
    print(contador)
    contador += 1



#CONTINUE

contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue
    print(contador)
