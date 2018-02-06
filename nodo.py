# -*- coding: utf-8 -*-

class NodoDT(object):
    
    def __init__(self, atributo = -1, distr = None, ramas = None, clase = None):
        
        """
        Diccionario donde la clave será cada una de las clases, y el valor
        el número de veces que ha aparecido. Ejemplo:
            {
                "concede": 15,
                "no concede": 5,
                "estudiar": 50
            }
        """
        self.distr = distr
        
        """
        Índice del atributo a estudiar. 
        Por ejemplo, en el caso de los préstamos:
            Empleo --> 0
            Productos --> 1
            Propiedades --> 2
            Hijos --> 3
            Etc.
        """
        self.atributo = atributo
        
        """
        Diccionario donde las claves serán los valores de los atributos, y el
        valor es un Nodo que representa a otra parte del árbol. Ejemplo:
            Si tenemos 'Empleo':
                {
                    parado : Nodo10,
                    funcionario: Nodo20,
                    laboral: Nodo5,
                    jubilado: Nodo1
                }
        """
        self.ramas = ramas
        
        """
        Si estamos en un Nodo hoja, este atributo tendrá la clase a la que
        pertenece el modelo dado.
        """
        self.clase = clase