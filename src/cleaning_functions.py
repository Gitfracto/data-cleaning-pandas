import numpy as np #np.nan y mucho mas
import pandas as pd #dataframe y mucho mas
import seaborn as sns #graficos
import matplotlib.pyplot as plt #graficos
from matplotlib.pyplot import figure #graficos 
import re # limpiar columnas 
from collections import Counter # limpiar columnas 
from operator import itemgetter # limpiar columnas


# Function to clean the age column:
# primero querias limpiar la data a numeros asi que en regex usuaste: 
# re.findall(r'\b\d+\b',x), donde r' empieza el string, \b\d+\d' recoge los numeros de principio a fin.
#Luego para que esa lista pasara a integros use: [int(i) for i in re.findall(r'\b\d+\b',x)]
#Para sacar la media en las listas con dos o mas edades coloque: np.mean([int(i) for i in re.findall(r'\b\d+\b',x)])
#por ultimo, para no tener float colocaste: int()

#ok, por que los loops? pues facil, me di cuenta que la lista puede estar vacia y que daba error
#por el mean, asi que le pedi que si la lista estaba vacia pues me diera unknow, sino, lo de arriba
def regex_age(x):
    if "month" in x:
        return "unknow"
    else:
        if [int(i) for i in re.findall(r'\b\d+\b',x)] == []:
            return "unknow"
        else:
            return int(np.mean([int(i) for i in re.findall(r'\b\d+\b',x)]))

####

# Function to clean the activity column:
# Con esta funcion obtengo los strings que tengan palabras que terminen en ing. el Redex similar al de arriba pero de palabras con \w
def regex_activity(x):
    return "".join(re.findall(r'\b(\w+ing)\b',x)).lower()
# luego use otra funcion para agrupar a los verbos en los mas comunes, como swimming, surfing etc
# cree la lista "nowater" afuera de la funcion por miedo a que se creara una nueva por cada variable "x", no se
#si es la mejor forma pero funciona bien

def activity_grouping(x):
    nowater =[]
    if "swimming" in x or "diving" in x or "snorkel" in x or "drown" in x or "float" in x:
        return "swimming"
    elif "surfing" in x or "board" in x or "paddl" in x: 
        return "surfing"
    elif "netting" in x or "fishing" in x or "shell" in x or "oyster" in x or "lobster" in x or "pearl" in x or "spear" in x or "harpoon" in x or "crab" in x or "shrimp" in x:
        return "fishing"
    elif "yacht" in x or "boat" in x or "kayak" in x or "canoe" in x or "kakay" in x or "sail" in x or "sink" in x or "ski" in x or "row" in x:
        return "vessel related"
    elif "collecting" in x or "washing" in x or "wading" in x or "stand" in x or "knee" in x or "walking" in x or "splash" in x or "bath" in x or "sitting" in x or "tread" in x:
        return "Close to the water"
    else:
        nowater.append(x)
        return "other activity"
 ######
# en esta funcion logre recoger los meses de la columna date, ya que todos tenian el mismo formato
def clean_date(x):
    if "jan" in x or "Jan" in x:
        return "January"
    elif "feb" in x or "Feb" in x:
        return "February"
    elif "mar" in x or "Mar" in x:
        return "March" 
    elif "apr" in x or "Apr" in x:
        return "April"
    elif "may" in x or "May" in x:
        return "May" 
    elif "jun" in x or "Jun" in x:
        return "June"
    elif "jul" in x or "Jul" in x:
        return "July" 
    elif "aug" in x or "Aug" in x:
        return "August"
    elif "sep" in x or "Sep" in x:
        return "September" 
    elif "oct" in x or "Oct" in x:
        return "October"
    elif "nov" in x or "Nov" in x:
        return "November" 
    elif "dec" in x or "Dec" in x:
        return "December"
    else: 
        return np.nan
    # pude usar redex pero queria intentarlo con estos loops
    
    #####
    # Con esta funcion lmpie la variable de type, basicamente dividiendolo en provoked and unprovoked
def clean_type(x):
    if x == "Unprovoked":
        return "Unprovoked"
    elif x == "Provoked":
        return "Provoked"
    else:
        return np.nan

    ###########
    # Con la siguiente funcion limpie la columna country, recogiendo los valores de los 5 paises mas grandes denominados por el diccionario que cree en el archivo principal.
def clean_country(x):
    if x == "USA":
        return x
    elif x == "AUSTRALIA":
        return x
    elif x == "SOUTH AFRICA":
        return x
    elif x == "PAPUA NEW GUINEA":
        return x
    elif x == "NEW ZEALAND":
        return x
    else:
        return np.nan
    
    #######
    
    # Como se puede ver arriba al principio intente que no hubiesen nan, luego decidi que si y converti todo lo que no era nan en nan en la ultima dataframe con la siguiente funcion:
    #se que no era lo mas eficiente pero cumple su funcion, luego ire funcion a funcion a poner el np.nan como se debe
def unknow_nan(x):
    if x == "unknow":
        return np.nan
    elif x == "other":
        return np.nan
    elif x == "return":
        return np.nan
    else:
        return x
    
    # there are many other functions used for cleaning the data, but those are from the libraries above, i
    #explain them all in the jupyter notebook