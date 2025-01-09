#Diseña  un algoritmo que determine si dos numeros son iwales usando funciones

def iwales(a,b):
    if (a==b):
        return (f"Los número {a} y {b} Son iwales")
    else:
        return (f"Los Números {a} y {b} son diferentes")

print(iwales(5,6))