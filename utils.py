# -*- coding: utf-8 -*-

from copy import deepcopy
from collections import defaultdict
from collections import Counter
import time
import math
import sys

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
Calcula la máxima frecuencia, dado un conjunto de datos de ejemplo
"""
def maxima_frecuencia(datos):
    key = max(datos, key=datos.get)
    return {key: datos[key]}


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