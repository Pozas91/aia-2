# -*- coding: utf-8 -*-

from clasificador import Clasificador
from clasificador_no_encontrado import ClasificadorNoEntrenado
import utils

class ClasificadorDR(Clasificador):
    
    def __init__(self, clasificacion, clases, atributos):
        Clasificador.__init__(self, clasificacion, clases, atributos)
        
    
    def entrena(self, entrenamiento):
        self.reglas = utils.obtener_total_reglas(self.atributos, entrenamiento, self.clases)
        
    """
    Recibe como argumento un conjunto de prueba y devuelve el rendimiento del
    modelo obtenido en el entrenamiento.
    """
    def evalua(self, prueba):
        if self.reglas:

            # Calcula ejemplos correctamente clasificados
            res = 0
            ejemplos = list(prueba)

            for x in ejemplos:
                y = list(x)
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