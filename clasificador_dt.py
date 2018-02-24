# -*- coding: utf-8 -*-

import utils
from clasificador import Clasificador
from clasificador_no_encontrado import ClasificadorNoEntrenado
from nodo import NodoDT


class ClasificadorDT(Clasificador):

    def __init__(self, clasificacion, clases, atributos):
        Clasificador.__init__(self, clasificacion, clases, atributos)
        self.__arbol = None

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

    def entrena(self, entrenamiento, validacion=None, medida='entropia', maxima_frecuencia=1.0, minimo_ejemplos=0.0):

        indice_atributos = utils.indice_atributos(self.atributos)
        arbol = self.entrena_recursiva(entrenamiento, indice_atributos, entrenamiento, maxima_frecuencia,
                                       minimo_ejemplos, medida)
        self.set_arbol(arbol)

    def entrena_recursiva(self, datos_iniciales, indice_atributos, datos, maxima_frecuencia, minimo_ejemplos, medida):

        nodo = None
        distribucion_total = utils.distribucion_clases(datos_iniciales)
        distribucion_actual = utils.distribucion_clases(datos)
        proporcion = utils.proporcion_datos(distribucion_actual)

        """
        Comprobar caso base por máxima frecuencia
        """
        max_frecuencia_key = utils.maxima_frecuencia(proporcion)
        maxima_frecuencia_alcanzada = proporcion[max_frecuencia_key] >= maxima_frecuencia

        """
        Comprobar caso base por mínimo ejemplos
        """
        datos_iniciales_totales = utils.total_datos_distribucion(distribucion_total)
        datos_actuales_totales = utils.total_datos_distribucion(distribucion_actual)
        minimo_ejemplos_alcanzados = (datos_iniciales_totales / datos_actuales_totales) <= minimo_ejemplos

        """
        Comprobar caso base no más atributos por recorrer
        """
        minimo_atributos_alcanzados = indice_atributos == {}

        if maxima_frecuencia_alcanzada or minimo_ejemplos_alcanzados or minimo_atributos_alcanzados:
            return NodoDT(atributo=None, distr=distribucion_actual, ramas=None, clase=max_frecuencia_key)
        else:

            """
            Según cojamos un criterio de medida u otro, nos dará un atributo,
            que será mejor explorar.
            """
            mejor_atributo = utils.criterio_decision(medida, datos, self.atributos, indice_atributos)
            mejor_indice = indice_atributos[mejor_atributo]
            nodo = NodoDT(atributo=mejor_indice, distr=distribucion_actual, ramas=None, clase=None)

            # Nos quedamos con todos los posibles valores para ese atributo
            valores = self.atributos[mejor_indice][1]

            # Borramos el atributo escogido para evitar volverlo a coger
            del indice_atributos[mejor_atributo]

            # Creamos las ramas que va a tener nuestro siguiente nodo
            ramas = dict()

            for valor in valores:

                nuevos_datos = utils.filtrar_nuevos_datos(datos, valor, mejor_indice)

                if not nuevos_datos:
                    """
                    Si no tenemos más datos, convertimos este valor de la rama
                    en un nodo hoja donde la clase será la mayoritaria.
                    """
                    ramas[valor] = NodoDT(atributo=None, distr=distribucion_actual, ramas=None,
                                          clase=max(distribucion_actual, key=distribucion_actual.get))
                else:
                    """
                    Si seguimos teniendo datos, volvemos a llamar a la función
                    recursiva, y le pasaremos una copia de los índices de los
                    atributos para no dañar los anteriores en las demás ramas.
                    """
                    ramas[valor] = self.entrena_recursiva(datos_iniciales, indice_atributos.copy(), nuevos_datos,
                                                          maxima_frecuencia, minimo_ejemplos, medida)

            nodo.ramas = ramas
        return nodo

    """
    Establece el nodo raiz del arbol entrenado
    """
    def set_arbol(self, arbol):
        self.__arbol = arbol

    """
    Obtiene el nodo raiz del arbol entrenado
    """
    def get_arbol(self):
        return self.__arbol

    """
        Recibe como argumento un ejemplo y devuelve el valor de clasificación
        según el modelo obtenido en el entrenamiento.
        """
    def clasifica(self, ejemplo):
        if (self.get_arbol()):
            return self.clasifica_recursiva(ejemplo, self.get_arbol())
        else:
            raise ClasificadorNoEntrenado('método clasifica')

    """
    Función recursiva para clasificar el ejemplo
    """
    def clasifica_recursiva(self, ejemplo, arbol):

        res = ""

        if not arbol.ramas:
            res = arbol.clase
        else:
            for rama in arbol.ramas:
                if ejemplo[arbol.atributo] == rama:
                    res = self.clasifica_recursiva(ejemplo, arbol.ramas[rama])

        return res

    """
    Recibe como argumento un conjunto de prueba y devuelve el rendimiento del
    modelo obtenido en el entrenamiento.
    """
    def evalua(self, prueba):
        if self.get_arbol():

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
        if self.get_arbol():
            print(self.get_arbol())
        else:
            raise ClasificadorNoEntrenado('método imprime')
