# -*- coding: utf-8 -*-


class Clasificador:

    def __init__(self, clasificacion, clases, atributos):
        self.clasificacion = clasificacion
        self.clases = clases
        self.atributos = atributos

    def entrena(self, entrenamiento, validacion=None):
        pass

    """
    Recibe como argumento un ejemplo y devuelve el valor de clasificación
    según el modelo obtenido en el entrenamiento.
    """

    def clasifica(self, ejemplo):
        pass

    """
    Recibe como argumento un conjunto de prueba y devuelve el rendimiento del
    modelo obtenido en el entrenamiento.
    """

    def evalua(self, prueba):
        pass

    """
    Imprime de forma legible el modelo obtenido en el entrenamiento.
    """

    def imprime(self):
        pass
