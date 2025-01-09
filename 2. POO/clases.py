class coche(): #en el paréntesis van los parámetros
#1. Se definen los ATRIBUTOS/datos/características
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = True
#2. Se definen los MÉTODOS/acciones/funcionalidades
    def estado(self, enmarcha):
        if (self.enmarcha==True):
            return 'El coche está en marcha'

micoche=coche()
a=micoche.estado(False)
print(a)