# -*- coding: utf-8 -*-

from collections import defaultdict

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