# -*- coding: utf-8 -*-

from collections import defaultdict
import time
import math

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
    
    key = max(datos, key = datos.get)
    return {key: datos[key]}

"""
Calcula la entropia de un conjunto de datos dada la distribución total.
"""    
def entropia(distribucion):
    
    res = 0
    total = sum([distribucion[key] for key in distribucion])
    
    for key in distribucion:
        p = distribucion[key] / total
        res += p * math.log(p, 2)

    return -res

"""
Calcula el grado de entropía del criterio de decisión. 
Media ponderada de los grados de entropía de los conjuntos obtenidos tras la decisión.
"""
def entropia_media_ponderada(distribucion):
    
    res = 0
    total = sum([distribucion[key] for key in distribucion])
    
    for key in distribucion:
        p = distribucion[key] / total
        entropia = - (p * math.log(p, 2))
        res += (math.fabs(distribucion[key]) / math.fabs(total)) * entropia

    return res