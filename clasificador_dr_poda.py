# -*- coding: utf-8 -*-

from clasificador_dr import ClasificadorDR
from copy import deepcopy
import utils


class ClasificadorDRPoda(ClasificadorDR):

    def __init__(self, clasificacion, clases, atributos):
        ClasificadorDR.__init__(self, clasificacion, clases, atributos)
        self.mejores_reglas = None
        self.mejor_rendimiento = 0.0

    """ El método entrena recibe argumentos adicionales especificos de este tipo de clasicador 
        al igual que en el clasicador anterior. El modelo obtenido es podado a posteriori usando para
        ello el conjunto de validación """

    def entrena(self, entrenamiento, validacion=None):

        ClasificadorDR.entrena(self, entrenamiento, validacion)

        continuar = True

        while continuar:

            # Sacamos el mejor rendimiento anterior
            rendimiento = self.evalua(validacion)

            # Pasamos a la función una copia del conjuntos de reglas actual
            reglas = deepcopy(self.reglas)

            # Dado un sólo paso
            resultado = self.poda(reglas, validacion)
            mejor_rendimiento, nuevas_reglas = resultado

            # Si el rendimiento que hemos conseguido es menor o igual que el rendimiento anterior, entonces paramos
            # de buscar
            if mejor_rendimiento <= rendimiento:
                continuar = False

            # Si el rendimiento que hemos conseguido es mayor establecemos reglas como las nuevas reglas
            else:
                self.reglas = nuevas_reglas

    def poda(self, reglas, validacion):

        mejor_rendimiento = 0
        mejor_reglas = []

        for i, tupla in enumerate(reglas[:-1]):

            # Post-poda por condiciones de una regla
            copia_reglas = deepcopy(reglas)
            condiciones, clase = copia_reglas[i]
            for j, condicion in enumerate(condiciones):

                # Obtenemos todas las condiciones menos la indicada y la establecemos en nuestro conjunto de reglas
                condiciones_reducidas = [x for k, x in enumerate(condiciones) if k != j]
                copia_reglas[i] = (condiciones_reducidas, clase)

                self.reglas = copia_reglas
                rendimiento = self.evalua(validacion)

                # Si su rendimiento ha mejorado, guardamos la información
                if rendimiento >= mejor_rendimiento:
                    mejor_reglas = deepcopy(self.reglas)
                    mejor_rendimiento = rendimiento

                # Restauramos la tupla original
                copia_reglas[i] = (condiciones, clase)

            # Post-poda por reglas completas
            copia_reglas = deepcopy(reglas)
            copia_reglas.pop(i)
            self.reglas = copia_reglas
            rendimiento = self.evalua(validacion)

            # Si su rendimiento ha mejorado, guardamos la información
            if rendimiento >= mejor_rendimiento:
                mejor_reglas = self.reglas
                mejor_rendimiento = rendimiento

        return (mejor_rendimiento, mejor_reglas)
