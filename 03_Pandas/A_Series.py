# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:15:57 2019

@author: LeAdm
"""
print("Hola mundo !!")

# Creando variables
nombre = "Criss"
edad = 25

print(nombre)

# Importando Numpy y Pandas
import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
numeros_serie = pd.Series(lista_numeros)
# Creando tuplas y enviandolo al constructor de la serie
tupla_numeros = (10,11,12,13)
np_numeros = np.array((1,2,3,4))

numeros_serieb = pd.Series(tupla_numeros)
numeros_seriec = pd.Series(np_numeros)

numeros_seried = pd.Series([
        True,
        False,
        12,
        12.21,
        "Criss",
        None,
        (),
        [],
        {"Nombre": "Criss"}])

## Poniendo índices a las variables:
lista_ciudades = ['Ambato','Cuenca','Loja','Quito']
#serie_ciudades = pd.Series(lista_ciudades, index=['4','5','1','17'])
serie_ciudades = pd.Series(lista_ciudades, index=['A','C','L','Q'])

# poniendo nombres a los índices
serie_ciudades['Q']
serie_ciudades[0]

print(type(serie_ciudades))

# diccionarios
valores_ciudad = {
        'Ibarra':9500,
        'Guayaquil': 10000,
        'Cuenca':7000,
        'Quito':8000,
        'Loja':3000
        }
serie_valor_ciudad = pd.Series(valores_ciudad)

serie_valor_ciudad['Ibarra']
serie_valor_ciudad[0]

## Ciudades menores a 5000?
ciudades_menores_5000 = serie_valor_ciudad < 5000
serie_menor_5000 = serie_valor_ciudad[ciudades_menores_5000]

# Operaciones dentro de ciudades??
# aumentar valores a todas las ciudades:
serie_valor_ciudad = serie_valor_ciudad * 1.1

# cambiar valor de la ciudad de Quito:
serie_valor_ciudad['Quito']=8750

# imprimir si una ciudad está dentro de la serie de ciudades?
print("Lima" in serie_valor_ciudad) # False
print("Loja" in serie_valor_ciudad) # True

# Series compatibles con numpy
np.square(serie_valor_ciudad)
np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({
        'Quito':1500,
        'Loja':4000,
        'Guayaquil':2000
        })
ciudades_dos = pd.Series({
        'Montañita':1500,
        'Guayaquil':4000,
        'Quito':2000
        })

print (ciudades_uno * ciudades_dos)
# >> Solo multiplica los campos con el mismo índice

# randómicos
randomico = np.random.rand(3)
serie_tres_rand = pd.Series(randomico)
ciudades_uno.index

# Concatenar series:
    ### suma los valores
ciudades_add = ciudades_dos.add(ciudades_uno)
ciudades_add

    ## concat
ciudades_concat = pd.concat([ciudades_uno,ciudades_dos])
ciudades_concat # --> Se repten los índices

    ## concat sin repeticion de indices
ciudades_concatv = pd.concat([ciudades_uno,ciudades_dos], verify_integrity= True)
ciudades_concatv

    ## append
ciudades_append = ciudades_uno.append(ciudades_dos)
ciudades_append

# Agregar un nuevo índice con un nuevo valor a la serie

# Minimo
ciudades_uno.min()
pd.Series.min(ciudades_uno)
np.max(ciudades_uno) #Numpy
# Maximo
ciudades_uno.max()
pd.Series.max(ciudades_uno) #Numpy
np.max(ciudades_uno)

# Estadísticas: Avg, Mean
ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

# Primeros 5
ciudades_uno.head(2)

# Ultimos 5
ciudades_uno.tail(2)

ciudades_uno.sort_values(ascending = False).head(2) # los dos máximos
ciudades_uno.sort_values(descending = False).tail(2) # los 2 mínimos

# Operaciones combinadas
# 0 >= 1000 -> 5%
# Con map:
def calculo(valor):
    if(valor <= 1000):
        return valor *1.05
    if(valor > 1000 and valor <= 10000):
        return valor *1.1
    if(valor > 10000):
        return valor *1.15
ciudades_uno.map(calculo)

#Con where:
# útil si existe solo una funcion
# ciudad_uno.where(ciudades_uno > 1000, ciudades_uno * 1.05)

# 1000 >= 10000 -> 10%
# 1000 >  -> 15%

