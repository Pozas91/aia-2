# -*- coding: utf-8 -*-

#Clase Excepción ClasificadorNoEntrenado
class ClasificadorNoEntrenado(Exception):
    
    def __init__(self, origen):

        # Call the base class constructor with the parameters it needs
        super(Exception, self).__init__("Exception: Clasificador no encontrador `{}`".format(origen))