class Interfaz():
    #Atributos
    Frecuencia_muestreo = 48000
    Canales = 2
    Respuesta_frecuencia = 30000
    Interruptor = 1
    Marca = 'Behringer'
    enREC = False
    #Métodos
    def Grabando(self, enREC):
        if (self.enREC==True):
            return 'Está grabando'
        else:
            o = 'No está grabando'
            return o
    def Detector(self, Frecuencia_muestreo):
        if (self.Frecuencia_muestreo>30000 and self.Frecuencia_muestreo<=48000):
            return 'Está funcionando bien! :D'
        else:
            return 'Hasta las huevas el muestreo pipipip :c'

miInterfaz = Interfaz()
a = miInterfaz.Grabando(True)
b = miInterfaz.Detector(48000)
print(a)
print(b)