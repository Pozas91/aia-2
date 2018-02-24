# -*- coding: utf-8 -*-

# Importaciones de librerías requeridas
from clasificador_dt import ClasificadorDT
from clasificador_dr import ClasificadorDR
import utils
from datasets.prestamos import clasificacion, atributos, clases, entrenamiento, validacion, prueba, ejemplo

# =============================================================================
# COMIENZO - TIEMPOS DE EJECUCIÓN
# =============================================================================
start_time = utils.comienzo_tiempo_ejecucion()

# =============================================================================
# INICIALIZACIÓN EL CLASIFICADOR DT
# =============================================================================
clasificador = ClasificadorDT(clasificacion, clases, atributos)

# =============================================================================
# INICIALIZACIÓN EL CLASIFICADOR DR
# =============================================================================
clasificador_dr = ClasificadorDR(clasificacion, clases, atributos)

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
clasificador.entrena(entrenamiento, medida = "gini")
clasificador_dr.entrena(entrenamiento)

# =============================================================================
# EVALUAMOS
# =============================================================================
evaluado = "Rendimiento: {}".format(clasificador.evalua(entrenamiento))
print(evaluado)

# =============================================================================
# CLASIFICAMOS
# =============================================================================
clasificado = "Clasificado: '{}'".format(clasificador.clasifica(ejemplo))
print(clasificado)

# =============================================================================
# FINAL - TIEMPOS DE EJECUCIÓN
# =============================================================================
utils.tiempo_ejecucion_obtenido(start_time)

utils.ejemplos_cubiertos([(0, 'parado'), (1, 'ninguno'), (3, 'dos o más')], entrenamiento)