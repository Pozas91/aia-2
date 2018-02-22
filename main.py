# -*- coding: utf-8 -*-

# Importaciones de librerías requeridas
from clasificador_dt import ClasificadorDT
from clasificador_dt_poda import ClasificadorDTPoda
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
clasificador_dt = ClasificadorDT(clasificacion, clases, atributos)

# =============================================================================
# INICIALIZACIÓN EL CLASIFICADOR DT PODA
# =============================================================================
clasificador_dt_poda = ClasificadorDTPoda(clasificacion, clases, atributos)

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
clasificador_dt.entrena(entrenamiento, medida="entropia")
clasificador_dt_poda.entrena(prueba, validacion=validacion, medida="entropia")

# =============================================================================
# EVALUAMOS
# =============================================================================
rendimiento = clasificador_dt.evalua(validacion)
evaluado = "Rendimiento base: {0:.1f}%".format(round(rendimiento * 100, 1))
print(evaluado)

rendimiento = clasificador_dt_poda.evalua(validacion)
evaluado = "Rendimiento con post-poda: {0:.1f}%".format(round(rendimiento * 100, 1))
print(evaluado)

# =============================================================================
# CLASIFICAMOS
# =============================================================================
clasificado = "Clasificado base: '{}'".format(clasificador_dt.clasifica(ejemplo))
print(clasificado)

clasificado = "Clasificado post-poda: '{}'".format(clasificador_dt_poda.clasifica(ejemplo))
print(clasificado)

# =============================================================================
# FINAL - TIEMPOS DE EJECUCIÓN
# =============================================================================
utils.tiempo_ejecucion_obtenido(start_time)
