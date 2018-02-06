# -*- coding: utf-8 -*-

#Importamos la excepción personalizada ClasificadorNoEntrenado
from clasificador_no_encontrado import ClasificadorNoEntrenado
from nodo import NodoDT

#Clase clasificador
class Clasificador:
    
    def __init__(self, clasificacion, clases, atributos):
        self.clasificacion = clasificacion
        self.clases = clases
        self.atributos = atributos
        self.__arbol = NodoDT()
        
    def entrena(self, entrenamiento, validacion = None):
        try:
            """ LÓGICA AQUÍ """
        except ClasificadorNoEntrenado:
            """ CONTROLAR EXCEPCIÓN AQUÍ """
    
    def clasifica(self, ejemplo):
        try:
            """ LÓGICA AQUÍ """
            raise ClasificadorNoEntrenado('método clasifica')
        except ClasificadorNoEntrenado as error:
            """ CONTROLAR EXCEPCIÓN AQUÍ """
            print(error)
    
    def evalua(self, prueba):
        try:
            """ LÓGICA AQUÍ """
            raise ClasificadorNoEntrenado('método evalua')
        except ClasificadorNoEntrenado as error:
            """ CONTROLAR EXCEPCIÓN AQUÍ """
            print(error)
    
    def imprime(self):
        try:
            """ LÓGICA AQUÍ """
            raise ClasificadorNoEntrenado('método imprime')
        except ClasificadorNoEntrenado as error:
            """ CONTROLAR EXCEPCIÓN AQUÍ """
            print(error)