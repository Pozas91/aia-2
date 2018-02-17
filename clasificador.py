# -*- coding: utf-8 -*-

#Importamos la excepción personalizada ClasificadorNoEntrenado
from clasificador_no_encontrado import ClasificadorNoEntrenado
from nodo import NodoDT

#Clase clasificador
class Clasificador:
    
    def __init__(self, clasificacion, clases, atributos):
        self.clasificacion = clasificacion
        self.clases = clases
        self.atributos = atributos
        self.__arbol = None
        
    def entrena(self, entrenamiento, validacion = None):
        try:
            """ LÓGICA AQUÍ """
        except ClasificadorNoEntrenado:
            """ CONTROLAR EXCEPCIÓN AQUÍ """
    
    """
    Recibe como argumento un ejemplo y devuelve el valor de clasificación
    según el modelo obtenido en el entrenamiento.
    """
    def clasifica(self, ejemplo):
        if(self.get_arbol()):
            
            res = ""
            arbol = self.get_arbol()
            
            if arbol.ramas != None:
                for rama in arbol.ramas:
                    if ejemplo[arbol.atributo] == rama:
                        res = self.clasifica(arbol.ramas[rama], ejemplo)
            else:
                res = arbol.clase
            
            return res
        else:
            raise ClasificadorNoEntrenado('método clasifica')
    
    """
    Recibe como argumento un conjunto de prueba y devuelve el rendimiento del
    modelo obtenido en el entrenamiento.
    """
    def evalua(self, prueba):
        if(self.get_arbol()):
             
            #Calcula ejemplos correctamente clasificados
            res = 0
            ejemplos = list(prueba)
            
            for x in ejemplos:
                y = list(x)
                clase = y.pop(-1)
                clase_rama = self.clasifica(y)
                if clase_rama == clase:
                    res += 1
            
            rendimiento = res / len(prueba)
            
            return rendimiento
        else:
            raise ClasificadorNoEntrenado('método evalua')
            
    """
    Imprime de forma legible el modelo obtenido en el entrenamiento.
    """
    def imprime(self):
        if(self.get_arbol()):
            print(self.get_arbol())
        else:
            raise ClasificadorNoEntrenado('método imprime')
            
    def set_arbol(self, arbol):
        self.__arbol = arbol
        
    def get_arbol(self):
        return self.__arbol