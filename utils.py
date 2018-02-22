# -*- coding: utf-8 -*-

from collections import defaultdict
from collections import Counter
import time
import math
import sys
from nodo import NodoDT

"""
Comprueba si un nodo de un arbol es interior
"""


def es_interior(nodo):
    if nodo.ramas:
        return len([rama for rama in nodo.ramas if rama]) > 0
    else:
        return False


'''
Obtiene el nodo raiz de un nuevo arbol que llega hasta el nodo intermedio indicado, que se convertirá en un nodo hoja.
'''
def obtener_nuevo_arbol(raiz, objetivo):
    return obtener_nuevo_arbol_recursivo(raiz, objetivo)

def obtener_nuevo_arbol_recursivo(actual, objetivo):

    if actual == objetivo:
        key = maxima_frecuencia(objetivo.distr)
        nodo = NodoDT(None, objetivo.distr, None, key)
    else:
        if actual.ramas:
            for key in actual.ramas:
                hijo = actual.ramas[key]
                actual.ramas[key] = obtener_nuevo_arbol_recursivo(hijo, objetivo)

        nodo = actual

    return nodo

"""
Crea un diccionario donde la clave es el nombre de la clase
y el valor es el número de veces que aparece esta.
"""


def distribucion_clases(datos):
    res = defaultdict(int)

    [res.update({x[-1]: res[x[-1]] + 1}) for x in datos]

    return res


"""
Crea un diccionario donde la clave es el nombre del atributo y el valor
es el índice de este.
"""


def indice_atributos(atributos):
    res = dict()

    [res.update({x[0]: atributos.index(x)}) for x in atributos]

    return res


"""
Función utilizada para capturar el momento en el que comienza todo.
"""


def comienzo_tiempo_ejecucion():
    # Variable usada para medir los tiempos de ejecución
    start_time = time.time()
    return start_time


"""
Función utilizada para calcular los tiempos de ejecución de la aplicación en base al comienzo.
"""


def tiempo_ejecucion_obtenido(start_time):
    # Tiempo de ejecución obtenido
    print("Tiempo de ejecución en segundos: --- %s seconds ---" % (time.time() - start_time))


"""
Calcula el total de datos pasando una distribución.
"""


def total_datos_distribucion(distribucion):
    return sum([distribucion[key] for key in distribucion])


"""
Calcula la proporción de los datos dados.
"""


def proporcion_datos(datos):
    result = dict()

    total = sum([datos[x] for x in datos])

    for key in datos:
        result[key] = datos[key] / total

    return result


"""
Devuelve la clave de la máxima frecuencia, dado un conjunto de datos de ejemplo
"""


def maxima_frecuencia(datos):
    return max(datos, key=datos.get)


"""
Calcula la tasa de error de un conjunto de datos.
"""


def tasa_error(S):
    total = total_datos_distribucion(S)
    key = max(S, key=S.get)
    Pd = S.get(key)

    return 1 - (Pd / total)


def tasa_error_media_ponderada(S, Si):
    total_S = total_datos_distribucion(S)
    total_Si = total_datos_distribucion(Si)

    return (total_Si / total_S) * tasa_error(Si)


"""
Calcula el índice de gini de un conjunto de datos.
"""


def gini(S):
    res = 0
    total = total_datos_distribucion(S)

    for key in S:
        p = S[key] / total
        res += math.pow(p, 2)

    return 1 - res


def gini_media_ponderada(S, Si):
    total_S = total_datos_distribucion(S)
    total_Si = total_datos_distribucion(Si)

    return (total_Si / total_S) * gini(Si)


"""
Calcula la entropia de un conjunto de datos dada la distribución total.
"""


def entropia(S):
    res = 0
    total = total_datos_distribucion(S)

    for key in S:
        p = S[key] / total
        res += p * math.log(p, 2)

    return -res


"""
Calcula el grado de entropía del criterio de decisión. 
Media ponderada de los grados de entropía de los conjuntos obtenidos tras la decisión.
"""


def entropia_media_ponderada(S, Si):
    total_S = total_datos_distribucion(S)
    total_Si = total_datos_distribucion(Si)

    return (total_Si / total_S) * entropia(Si)


"""
Calcula la ganacia de información
"""


def ganancia_informacion(S, Si):
    # TODO
    return entropia(S) - entropia(S)


"""
Calcula la media ponderada según el criterio de medida
"""


def calcular_media_ponderada(medida, S, Si):
    if (medida == "entropia"):
        resultado = entropia_media_ponderada(S, Si)
    elif (medida == "error"):
        resultado = tasa_error_media_ponderada(S, Si)
    elif (medida == "gini"):
        resultado = gini_media_ponderada(S, Si)
    else:
        raise ValueError("La medida {} no está registrada.".format(medida))

    return resultado


"""
Selecciona la mejor opción para elegir qué rama es mejor explorar
"""


def criterio_decision(medida, datos, atributos, indice_atributos):
    S = distribucion_clases(datos)
    Si = []
    Si_dict = dict()

    # Buscamos en cada atributo restante
    for atributo, indice in indice_atributos.items():
        for valor in atributos[indice][1]:
            # Cogemos los datos correspondientes a ese atributo y valor
            datos_filtrados = [dato for dato in datos if dato[indice] == valor]

            # Realizamos la distribución de cada conjunto de datos
            Si.append(distribucion_clases(datos_filtrados))

        Si_dict.update({atributo: Si})
        Si = []

    """
    Declaramos la variable total para calcular cada una de las medias
    ponderadas
    """
    total = 0
    minimo = sys.maxsize
    mejor_atributo = ""

    for atributo in Si_dict:
        for Si in Si_dict[atributo]:

            # Si 'Si' no está vacio calculo su media
            if not not Si:
                total += calcular_media_ponderada(medida, S, Si)

        if (total <= minimo):
            minimo = total
            mejor_atributo = atributo

    return mejor_atributo


"""
Obtiene un nuevo conjunto de datos
"""


def filtrar_nuevos_datos(datos, valor, indice):
    nuevos_datos = []

    for dato in datos:
        if valor in dato[indice]:
            nuevos_datos.append(dato)

    return nuevos_datos


"""
Obtener la categoría con más frecuencia
"""


def obtener_frecuencia_ordenada(lista):
    dict_aux = distribucion_clases(lista)
    resultado = dict()
    [resultado.update({k: dict_aux[k]}) for k in sorted(dict_aux, key=dict_aux.get)]
    return resultado


"""
Devuelve los ejemplos cubiertos que quedan cubiertos por la regla R en el conjunto de datos D
"""


def ejemplos_cubiertos(R, D):
    ejemplos_cubiertos = D

    for condicion in R:
        indice_atributo, valor = condicion
        ejemplos_cubiertos = [ejemplo for ejemplo in ejemplos_cubiertos if ejemplo[indice_atributo] == valor]

    return ejemplos_cubiertos


"""
Devuelve los ejemplos que están correctamente cubiertos por la regla R en el conjunto de datos D, y que coincidan con
la clase C.
"""


def ejemplos_correctamente_cubiertos(R, D, C):
    ejemplos = ejemplos_cubiertos(R, D)

    return [ejemplo for ejemplo in ejemplos if ejemplo[-1] == C]


"""
Devuelve la frecuencia relativa para la regla R, en el conjunto de datos D, y para la clase C
"""


def frecuencia_relativa(R, D, C):
    t = len(ejemplos_cubiertos(R, D))
    p = len(ejemplos_correctamente_cubiertos(R, D, C))

    return p / t


"""
Una funcion que dada los atributos y un conjuntos de datos, devuelva una regla para ese conjunto de datos
"""

"""
Una funcion que para una clase entera, devuelva todas las reglas de esa clase,
itera sobre la anterior y con el resto de atributos que no estén cubiertos por esa primera regla, se llama a la anterior
con el conjunto de ejemplos restante para crear otra regla, hasta que no queden ejemplos
"""

"""
Por último, otra que itere sobre todas las clases y llame a la anterior, pero en esta funcion en concreto no se reducen
los ejemplos.
"""
