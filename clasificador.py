# -*- coding: utf-8 -*-

# Importamos la excepción personalizada ClasificadorNoEntrenado
from clasificador_no_encontrado import ClasificadorNoEntrenado

# Clase clasificador
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
            return self.clasifica_recursiva(ejemplo, self.get_arbol())
        else:
            raise ClasificadorNoEntrenado('método clasifica')
          
    """
    Función recursiva para clasificar el ejemplo
    """
    def clasifica_recursiva(self, ejemplo, arbol):
        
        res = ""
        
        if not arbol.ramas:
            res = arbol.clase
        else:
            for rama in arbol.ramas:
                if ejemplo[arbol.atributo] == rama:
                    res = self.clasifica_recursiva(ejemplo, arbol.ramas[rama])
            
        return res
    
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
            
            return "{0:.1f}%".format(round(rendimiento * 100, 1))
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