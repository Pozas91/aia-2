# -*- coding: utf-8 -*-

from clasificador_dt import ClasificadorDT
from copy import deepcopy
from nodo import NodoDT
import utils


class ClasificadorDTPoda(ClasificadorDT):

    def __init__(self, clasificacion, clases, atributos):
        ClasificadorDT.__init__(self, clasificacion, clases, atributos)

    """ El método entrena recibe argumentos adicionales especificos de este tipo de clasicador 
        al igual que en el clasicador anterior. El modelo obtenido es podado a posteriori usando para
        ello el conjunto de validación """

    def entrena(self, entrenamiento, validacion=None, medida='entropía', maxima_frecuencia=1.0, minimo_ejemplos=0.0):

        ClasificadorDT.entrena(self, entrenamiento, validacion, medida, maxima_frecuencia, minimo_ejemplos)

        rendimiento_base = self.evalua(validacion)
        arbol_base = self.get_arbol()
        arbol = deepcopy(arbol_base)
        arboles = dict()

        self.poda_ramas_recursiva(arbol, validacion, arboles)

        mejor_arbol = utils.maxima_frecuencia(arboles)
        print(arboles[mejor_arbol])

    def poda_ramas_recursiva(self, arbol, validacion, arboles):

        copia = deepcopy(arbol)

        for key in arbol.ramas:
            hijo = arbol.ramas[key]

            if not hijo.ramas:
                key = utils.maxima_frecuencia(arbol.distr)
                arbol.atributo = None
                arbol.ramas = None
                arbol.clase = key
                self.set_arbol(arbol)
                arboles.update({arbol: self.evalua(validacion)})
            else:
                self.poda_ramas_recursiva(hijo, validacion, arboles)

            arbol = deepcopy(copia)
