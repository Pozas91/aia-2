# -*- coding: utf-8 -*-

#Importamos la clase padre Clasificador
from clasificador import Clasificador

#Clase ClasificadorDTPoda
class ClasificadorDTPoda(Clasificador):
    
    def __init__(self, clasificacion, clases, atributos):
        self.clasificacion = clasificacion
        self.clases = clases
        self.atributos = atributos
    

    """ El método entrena recibe argumentos adicionales especificos de este tipo de clasicador 
        al igual que en el clasicador anterior. El modelo obtenido es podado a posteriori usando para
        ello el conjunto de validación """    
    def entrena(self, entrenamiento, validacion = None, medida = 'entropía', maxima_frecuencia = 1.0, minimo_ejemplos = 0.0):
        
        pass
        