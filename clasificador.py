# -*- coding: utf-8 -*-

#Importamos la excepción personalizada ClasificadorNoEntrenado
from clasificador_no_encontrado import ClasificadorNoEntrenado

#Clase clasificador
class Clasificador:
    
    def __init__(self, clasificacion, clases, atributos):
        self.clasificacion = clasificacion
        self.clases = clases
        self.atributos = atributos
        
    def entrena(self, entrenamiento, validacion = None):
        try:
            """ LÓGICA AQUÍ """
        except ClasificadorNoEntrenado:
            """ CONTROLAR EXCEPCIÓN AQUÍ """
    
    """
    Recibe como argumento un ejemplo y devuelve el valor de clasificación
    según el modelo obtenido en el entrenamiento.
    """
    def clasifica(self, ejemplo):
        try:
            """ LÓGICA AQUÍ """
            raise ClasificadorNoEntrenado('método clasifica')
        except ClasificadorNoEntrenado as error:
            """ CONTROLAR EXCEPCIÓN AQUÍ """
            print(error)
    
    """
    Recibe como argumento un conjunto de prueba y devuelve el rendimiento del
    modelo obtenido en el entrenamiento.
    """
    def evalua(self, prueba):
        try:
            """ LÓGICA AQUÍ """
            raise ClasificadorNoEntrenado('método evalua')
        except ClasificadorNoEntrenado as error:
            """ CONTROLAR EXCEPCIÓN AQUÍ """
            print(error)
    
    """
    Imprime de forma legible el modelo obtenido en el entrenamiento.
    """
    def imprime(self):
        try:
            """ LÓGICA AQUÍ """
            raise ClasificadorNoEntrenado('método imprime')
        except ClasificadorNoEntrenado as error:
            """ CONTROLAR EXCEPCIÓN AQUÍ """
            print(error)