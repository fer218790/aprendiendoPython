def suma_elementos(lista):
    suma=0          #Inicializamos valores
    for i in lista: #Iteramos la lista "lista"
        suma+=i     #Sumamos y almacenamos en "suma"
    return suma     #regresamos el valor de "suma"

resultado = suma_elementos([1,2,3])
print(f"asaa: {resultado}")

###otra manera

def suma_elementor(listar):
    return sum(listar) #función sum() suma todos los elemtnos de una lista

resultado = suma_elementor([1,2,3])
print(f"La suma es: {resultado}")
