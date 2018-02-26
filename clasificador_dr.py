# -*- coding: utf-8 -*-

from clasificador import Clasificador
from clasificador_no_encontrado import ClasificadorNoEntrenado
import utils
from copy import deepcopy


class ClasificadorDR(Clasificador):

    def __init__(self, clasificacion, clases, atributos):
        Clasificador.__init__(self, clasificacion, clases, atributos)
        self.reglas = []

    def entrena(self, entrenamiento, validacion=None):
        self.reglas = utils.obtener_total_reglas(self.atributos, entrenamiento, self.clases)

    """
    Recibe como argumento un ejemplo y devuelve el valor de clasificación
    según el modelo obtenido en el entrenamiento.
    """

    def clasifica(self, ejemplo):
        if self.reglas:

            for regla, clase in self.reglas:

                # Si la regla es None, hemos llegado a la de por defecto
                if not regla:
                    return clase
                else:
                    clasificado = True
                    # Veremos si nuestro ejemplo coincide con una regla completa
                    for condicion in regla:
                        indice, valor = condicion
                        clasificado = clasificado and ejemplo[indice] == valor

                        # En el momento que una condición no cumpla evitamos comprobar el resto de ellas
                        if not clasificado:
                            break

                    if clasificado:
                        return clase
        else:
            raise ClasificadorNoEntrenado('método clasifica')

    """
    Recibe como argumento un conjunto de prueba y devuelve el rendimiento del
    modelo obtenido en el entrenamiento.
    """

    def evalua(self, prueba):
        if self.reglas:

            # Calcula ejemplos correctamente clasificados
            res = 0

            for x in prueba:
                y = deepcopy(x)
                clase = y.pop(-1)
                clase_rama = self.clasifica(y)
                if clase_rama == clase:
                    res += 1

            rendimiento = res / len(prueba)

            return rendimiento
        else:
            raise ClasificadorNoEntrenado('método evalua')

    """
    Imprime de forma legible el modelo obtenido en el entrenamiento.
    """

    def imprime(self):
        if self.reglas:
            print(self.reglas)
        else:
            raise ClasificadorNoEntrenado('método imprime')
