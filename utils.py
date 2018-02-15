# -*- coding: utf-8 -*-

from collections import defaultdict
import time

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