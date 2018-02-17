# -*- coding: utf-8 -*-

# Importaciones de librerías requeridas
from copy import deepcopy
from collections import defaultdict
from clasificador_dt import ClasificadorDT
from utils import *
from datasets.prestamos import clasificacion, atributos, clases, entrenamiento, validacion, prueba

# =============================================================================
# COMIENZO - TIEMPOS DE EJECUCIÓN
# =============================================================================
start_time = comienzo_tiempo_ejecucion()

# =============================================================================
# INICIALIZACIÓN EL CLASIFICADOR DT
# =============================================================================
clasificador = ClasificadorDT(clasificacion, clases, atributos)

# =============================================================================
# INFORMACIÓN UTILIZADA DEL DATASET
# =============================================================================
print("Clasificación: " + clasificacion)
print("Atributos: [{0}]".format(', '.join(map(str, atributos))))
print("Clases: [{0}]".format(', '.join(map(str, clases))))
print("Conjunto de entrenamiento: [{0}]".format(', '.join(map(str, entrenamiento))))
print("Conjunto de validacion: [{0}]".format(', '.join(map(str, validacion))))
print("Conjunto de prueba: [{0}]".format(', '.join(map(str, prueba))))

print("*************************************************")

# =============================================================================
# ENTRENAMOS
# =============================================================================
clasificador.entrena(entrenamiento)

# =============================================================================
# EVALUAMOS
# =============================================================================
clasificador.evalua(entrenamiento)

# =============================================================================
# CLASIFICAMOS
# =============================================================================
clasificador.clasifica(entrenamiento)

# =============================================================================
# FINAL - TIEMPOS DE EJECUCIÓN
# =============================================================================
tiempo_ejecucion_obtenido(start_time)