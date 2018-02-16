# -*- coding: utf-8 -*-

# Importaciones de librerías requeridas
from copy import deepcopy
from collections import defaultdict
from clasificador_dt import ClasificadorDT
from utils import *
from datasets.prestamos import clasificacion, atributos, clases, entrenamiento
import math

# Variables globales


# Variable usada para medir los tiempos de ejecución
start_time = comienzo_tiempo_ejecucion()


clasificador = ClasificadorDT(clasificacion, clases, atributos)
clasificador.entrena(entrenamiento)


# Tiempo de ejecución obtenido
tiempo_ejecucion_obtenido(start_time)

def entropia(ejemplos, totalclases, inicial):

    dist = defaultdict(int)
    numeroclases = 0
    res = 0.0
    
    for x in ejemplos:
        y = x[-1]
        if y in dist:
            dist[y] += 1
            numeroclases += 1
        else:
            dist[y] = 1
            numeroclases += 1

    print(dist, numeroclases)
    if inicial:
        for x in dist:
            res = res - (dist[x]/numeroclases) * math.log((dist[x]/numeroclases),2)
    else:
        for x in dist:
            res = res - (numeroclases/totalclases)*(- dist[x]/numeroclases)* math.log((dist[x]/numeroclases),2)

    return res