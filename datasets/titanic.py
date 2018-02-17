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