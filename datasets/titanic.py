# =============================================================================
# CONJUNTO DE DATOS SACADO DEL TITANIC (titanic.txt)
# =============================================================================

import random
path = "titanic.txt"

# =============================================================================
# PROCESAMOS LOS DATOS DEL FICHERO
# =============================================================================

atributos = [("Clase",["1st","2nd","3rd"]),("Edad",["0","1","2"]),("Género",["male","female"])]

# El atributo de clasificación indica si se sobrevive o no
clasificacion = 'Supervivencia'

# Las clases representan al atributo Edad que según el corte establecido de edad representa vive (1) o muere (0)
clases = ['0', '1']

# Función utilizada para realizar asignar 0, 1 y 2 en función de la edad y su expectativa de vida
def corte_edad(edad):
    res = ""
    
    if edad == 'NA':
        edad = random.randint(1,100)
    else:
        edad = float(edad)
    
    if (edad <= 13):
        res = "0"
    elif (edad >= 60):
        res = "1"
    else:
        res = "2"
        
    return res

# Función utilizada para crear un conjunto de datos (Entrenamiento, Validación y Prueba)
# =============================================================================
#         append: Appends object at end.
# 
#         x = [1, 2, 3]
#         x.append([4, 5])
#         print (x)
#         gives you: [1, 2, 3, [4, 5]]
#         
#         extend: Extends list by appending elements from the iterable.
#         
#         x = [1, 2, 3]
#         x.extend([4, 5])
#         print (x)
#         gives you: [1, 2, 3, 4, 5]
#
#         list2 = [1, 2, 3, 4, 5, 6, 7 ];
#         print "list2[1:5]: ", list2[1:5]
#         list2[1:5]:  [2, 3, 4, 5]
# =============================================================================
def genera_ejemplos(datos,proporcion):
    datos_dict = dict()
    lista_resultante = list()
    
    for atributo in atributos[0][1]:
        listaAux = list()
        
        for titanic in titanic_list:
            if titanic[0] == atributo:
                listaAux.append(titanic)
        
        # Calcumos el indice a través del tamaño de la lista y la proporción dada. 
        # Nos quedamos hasta el último índice que cumple esta restricción        
        indice_lista = int(len(listaAux)*proporcion)
        # Añadimos en nuestra lista resultante todos los ejemplos
        lista_resultante.extend(listaAux[datos[atributo]:datos[atributo]+indice_lista])
        # Almacenamos en el diccionario el indice recorrido en cada iteración por cada atributo
        datos_dict[atributo] = indice_lista
    
    # Almaceno en la posición 0 la lista resultante con todos los ejemplos    
    datos_dict[0] = lista_resultante
    
    return datos_dict

# Abrimos el fichero titanic.txt para recorrer toda la información incrustada en el fichero
with open(path, "r", encoding="utf8") as file:
    
    # Ejecutamos el método next(file) para saltarnos la primera linea que incluye las cabeceras
    next(file)
    
    titanic_dict = dict()
    
    for line in file.readlines():
        titanic = []
        
        # Eliminamos la coma y quitamos aquellos campos que se encuentren vacios o nulos
        f_aux = line.replace(",","").split('"')
        f_aux = [x for x in f_aux if x]
        
        # Clase
        titanic.append(f_aux[1])
        
        # Supervivencia
        titanic.append(f_aux[2])
        
        # Edad
        titanic.append(corte_edad(f_aux[4]))
        
        # Género
        titanic.append(f_aux[-2])
        
        titanic_dict[int(f_aux[0])] = titanic
        
    file.close()
    
# Almacenamos en una lista todo el contenido del diccionario
titanic_list = list()
for titanic_dict_index in titanic_dict:
    titanic_list.append(titanic_dict[titanic_dict_index])

# =============================================================================
# CONJUNTO DE ENTRENAMIENTO
# =============================================================================
entrenamientoAux = genera_ejemplos({"1st":0,"2nd":0,"3rd":0}, 0.6)
entrenamiento = entrenamientoAux[0]

# =============================================================================
# CONJUNTO DE VALIDACIÓN
# =============================================================================
validacionAux = genera_ejemplos(entrenamientoAux, 0.2)
validacion = validacionAux[0]

# =============================================================================
# CONJUNTO DE PRUEBA
# =============================================================================
pruebaAux = genera_ejemplos(validacionAux, 0.2)
prueba = pruebaAux[0]