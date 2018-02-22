# -*- coding: utf-8 -*-

from clasificador_dt import ClasificadorDT
from copy import deepcopy
from nodo import NodoDT
import utils


class ClasificadorDTPoda(ClasificadorDT):

    def __init__(self, clasificacion, clases, atributos):
        ClasificadorDT.__init__(self, clasificacion, clases, atributos)
        self.mejor_arbol = None
        self.mejor_rendimiento = 0.0

    """ El método entrena recibe argumentos adicionales especificos de este tipo de clasicador 
        al igual que en el clasicador anterior. El modelo obtenido es podado a posteriori usando para
        ello el conjunto de validación """

    def entrena(self, entrenamiento, validacion=None, medida='entropía', maxima_frecuencia=1.0, minimo_ejemplos=0.0):

        ClasificadorDT.entrena(self, entrenamiento, validacion, medida, maxima_frecuencia, minimo_ejemplos)

        continuar = True

        while continuar:

            # Sacamos el mejor rendimiento anterior
            rendimiento = self.evalua(validacion)

            # Pasamos a la función una copia del arbol actual
            arbol = deepcopy(self.get_arbol())

            # Buscamos podando ramas, un arbol con un rendimiento mayor
            self.poda_recursiva(arbol, arbol, validacion)

            # Si el rendimiento que hemos conseguido es menor o igual que el rendimiento anterior, entonces paramos
            # de buscar
            if self.mejor_rendimiento <= rendimiento:
                continuar = False
            # Si el rendimiento que hemos conseguido es mayor establecemos mejor arbol como el nuevo arbol
            else:
                self.set_arbol(self.mejor_arbol)

    def poda_recursiva(self, raiz, nodo, validacion):

        copia_raiz = deepcopy(raiz)

        # Si es un nodo interior
        if utils.es_interior(nodo):

            '''
            Generamos un nuevo arbol desde el nodo raiz hasta el nodo interior, convirtiéndo el nodo interior
            en un nodo hoja. 
            '''
            nuevo_arbol = utils.obtener_nuevo_arbol(copia_raiz, nodo)

            # Lo asignamos a nuestro clasificador y comprobamos el rendimiento
            self.set_arbol(nuevo_arbol)
            rendimiento = self.evalua(validacion)

            if rendimiento >= self.mejor_rendimiento:
                self.mejor_arbol, self.mejor_rendimiento = nuevo_arbol, rendimiento

            # Volvemos a restaurar al arbol anterior
            self.set_arbol(raiz)

            # Y volvemos a hacer la comprobación para cada hijo
            for key in nodo.ramas:
                nodo_hijo = nodo.ramas[key]
                self.poda_recursiva(raiz, nodo_hijo, validacion)

