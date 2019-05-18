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












