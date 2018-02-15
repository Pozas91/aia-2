# -*- coding: utf-8 -*-

from clasificador import Clasificador
from nodo import NodoDT
import utils

class ClasificadorDT(Clasificador):
    
    def __init__(self, clasificacion, clases, atributos):
        Clasificador.__init__(self, clasificacion, clases, atributos)
        
    """
    Recibe un conjunto de entrenamiento, un posible conjunto de validación que
    ayudará a evitar el sobreajuste.
    
    El atributo 'medida' indica la función que se utilizará para cuantificar el
    grado de clasificación. Sus valores deben ser error, gini o entropía e
    indican que se debe usar la tasa de error, el índice de Gini o la entropía
    (respectivamente). El valor por defecto será 'entropía'.
    
    El atributo 'maxima_frecuencia', es un valor entre 0 y 1 (por defecto 1).
    Es el umbral de la proporción de la clase dominante de los datos de un nodo
    por encima del cual el nodo no es candidato a nodo interno.
    
    El atributo 'minimo_ejemplos', es un valor entre 0 y 1 (por defecto 0). Es
    el umbral de la proporción de los datos de un nodo (con respecto al total
    de ejemplos) por debajo del cual el nodo no es candidato a nodo interno.
    """
    def entrena(self, entrenamiento, validacion = None, medida = 'entropía', maxima_frecuencia = 1.0, minimo_ejemplos = 0.0):
        
        arbol = self.id3(entrenamiento, self.atributos)
        
        utils.distribucion_clases(entrenamiento)
        
        self.set_arbol(arbol);
            
        pass
    
    def id3(self, datos_totales, atributos):
        return NodoDT()
    
    def id3_recursiva(datos_totales, atributos, datos_actuales):
        pass