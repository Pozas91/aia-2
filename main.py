# -*- coding: utf-8 -*-

# Importaciones de librerías requeridas
from copy import deepcopy
from collections import defaultdict
from clasificador_dt import ClasificadorDT
from utils import *
from datasets.prestamos import clasificacion, atributos, clases, entrenamiento, validacion, prueba
import math

# Variables globales


# Variable usada para medir los tiempos de ejecución
start_time = comienzo_tiempo_ejecucion()

clasificador = ClasificadorDT(clasificacion, clases, atributos)
clasificador.entrena(entrenamiento)
clasificador.evalua(prueba)
#print(clasificador.clasifica(entrenamiento))
#print(clasificador.clasifica(validacion))
#print(clasificador.clasifica(prueba))
#clasificador.imprime()
#entropia(clasificador.get_arbol().distr)
#entropia_media_ponderada(clasificador.get_arbol().distr)

# Tiempo de ejecución obtenido
tiempo_ejecucion_obtenido(start_time)