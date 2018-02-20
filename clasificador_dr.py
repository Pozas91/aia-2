# -*- coding: utf-8 -*-

from clasificador import Clasificador
from nodo import NodoDT
import utils

class ClasificadorDR(Clasificador):
    
    def __init__(self, clasificacion, clases, atributos):
        Clasificador.__init__(self, clasificacion, clases, atributos)
    
# =============================================================================
#         Una regla tiene la siguiente forma:
#
#           [condicion, condicion, condicion]
#           condicion = (indice_atributo, valor_deseado)
#           [(indice, valor), (indice, valor), (indice, valor)]
#
#         
#         reglas = [
#             ([(1, 'uno'), (0, 'parado'), (3, 'dos o mas')], 'estudiar'),
#             ([(1, 'dos'), (0, 'parado'), (3, 'dos o mas')], 'no conceder'),
#         ]
#
#         TENER EN CUENTA QUE SI HAY EMPATE ENTRE FRECUENCIA RELATIVA COGEMOS LA QUE MÁS CUBRA
#         Y SI NOS QUEDAMOS SIN EJEMPLOS TAMBIÉN PARA
#             
#         donde cada tupla tiene en su primera posición el indice correspondiente al atributo y su segunda posición
#         equivale al valor de dicho atributo
#         
#         POSICIÓN 0 -> EMPLEO, 
#         POSICIÓN 1 -> PRODUCTO, 
#         POSICIÓN 2 -> PROPIEDADES
#         POSICIÓN 3 -> HIJOS
#         POSICIÓN 4 -> ESTADO CIVIL
#         POSICIÓN 5 -> INGRESOS
# =============================================================================
    
    def entrena(self, entrenamiento, validacion = None):
        categorias = utils.obtener_frecuencia_ordenada(entrenamiento)
        reglas = list()
        regla_list = list()
        indice_atributos = utils.indice_atributos(self.atributos)
    
        for atributo in indice_atributos:
            indice_atributo = indice_atributos[atributo]
            
            for 
                
                
                
                
                
                
                
                
            