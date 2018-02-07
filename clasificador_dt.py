# -*- coding: utf-8 -*-

from clasificador import Clasificador
from nodo import NodoDT
from collections import defaultdict

class ClasificadorDT(Clasificador):
    
    def __init__(self, clasificacion, clases, atributos):
        Clasificador.__init__(self, clasificacion, clases, atributos)
        
    """
    Recibe un conjunto de entrenamiento, un posible conjunto de validación que
    ayudará a evitar el sobreajuste.
    
    El atributo 'medida' indica la función que se utilizará para cuentificar el
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
        
        distr = defaultdict(int)
        
        for x in self.clases:
            total = len([y for y in entrenamiento if y[-1] == x])
            distr.update({x : total})
        
        raiz = NodoDT(0, distr)
        print(raiz, distr)
        pass
    
    def funcion_recursiva_base():
        pass
    
    def funcion_recursiva():
        pass