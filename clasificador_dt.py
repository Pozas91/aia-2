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
    por encima del cual el nodo no es candidato a nodo interno, y se convertirá
    en un nodo hoja con la clase mayoritaria.
    
    El atributo 'minimo_ejemplos', es un valor entre 0 y 1 (por defecto 0). Es
    el umbral de la proporción de los datos de un nodo (con respecto al total
    de ejemplos) por debajo del cual el nodo no es candidato a nodo interno.
    """
    def entrena(self, entrenamiento, validacion = None, medida = 'entropía', maxima_frecuencia = 1.0, minimo_ejemplos = 0.0):
        
        indice_atributos = utils.indice_atributos(self.atributos)
        arbol = self.entrena_recursiva(entrenamiento, self.atributos, indice_atributos, entrenamiento, maxima_frecuencia, minimo_ejemplos)
        self.set_arbol(arbol);
    
    def entrena_recursiva(self, datos_iniciales, atributos, indice_atributos, datos, maxima_frecuencia, minimo_ejemplos):
        
        nodo = None
        distribucion = utils.distribucion_clases(datos)
        proporcion = utils.proporcion_datos(distribucion)
        frecuencia = utils.maxima_frecuencia(proporcion)
        max_frecuencia_key = next(iter(frecuencia))
        
        maxima_frecuencia_alcanzada = frecuencia[max_frecuencia_key] >= maxima_frecuencia
        # Pendiente
        minimo_ejemplos_alcanzados = True
        
        if(maxima_frecuencia_alcanzada or minimo_ejemplos_alcanzados):
            return NodoDT(atributo = None, distr = datos, ramas = None, clase = max_frecuencia_key)
        else:
            nodo = NodoDT(atributo = indice_atributos)
        
        return nodo