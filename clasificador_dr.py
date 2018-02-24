# -*- coding: utf-8 -*-

from clasificador import Clasificador
from nodo import NodoDT
import utils

class ClasificadorDR(Clasificador):
    
    def __init__(self, clasificacion, clases, atributos):
        Clasificador.__init__(self, clasificacion, clases, atributos)
        
    
    def entrena(self, entrenamiento, validacion = None):
        pass         