# -*- coding: utf-8 -*-

# Importaciones de librerías requeridas
import time
from copy import deepcopy
from collections import defaultdict
from clasificador_dt import ClasificadorDT
from datasets.prestamos import clasificacion, atributos, clases, entrenamiento

# Variables globales


# Variable usada para medir los tiempos de ejecución
start_time = time.time()


clasificador = ClasificadorDT(clasificacion, clases, atributos)
clasificador.entrena(entrenamiento)


# Tiempo de ejecución obtenido
print("Tiempo de ejecución en segundos: --- %s seconds ---" % (time.time() - start_time))