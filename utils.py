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
    
    key = max(datos, key = datos.get)
    return {key: datos[key]}

"""
Calcula la entropia de un conjunto de datos dada la distribución total.
"""    
def entropia(distribucion):
    
    res = 0
    total = total_datos_distribucion(distribucion)
    
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
    total = total_datos_distribucion(distribucion)
    
    for key in distribucion:
        p = distribucion[key] / total
        entropia = -(p * math.log(p, 2))
        res += (distribucion[key] / total) * entropia

    return res

"""
Selecciona la mejor opción para elegir qué rama es mejor explorar
"""
def criterio_decision(medida, datos, atributos, indice_atributos):
    
    mejor_atributo = next(iter(indice_atributos))
    
    if(medida == "entropia"):
        pass
    elif(medida == "error"):
        pass
    elif(medida == "gini"):
        pass
    else:
        raise ValueError("La medida {} no está registrada.".format(medida))
    
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
    