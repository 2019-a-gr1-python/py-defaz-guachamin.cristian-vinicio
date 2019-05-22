# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:53:38 2019

@author: LeAdm
"""
import pandas as pd
import os

path = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/03_Pandas/data/csv/artwork_data.csv'

df = pd.read_csv(
        path,
        nrows=5, #lee las 5 primeras filas
        usecols=['id','artist'],
        index_col='id'
        )
columnas_a_usar = ['id','artist','title','medium',
                   'year','acquisitionYear','height',
                   'width','units']

# cargando todos los datos
df_completo = pd.read_csv(
        path,
        usecols=columnas_a_usar,
        index_col='id'
        )

#evitar leer el csv a cada rato:
# erializar info en un archivo, si e necesita trabajar con el archivo, 
# se deserializa y podremos usar el dataframe.

path_guardado = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/03_Pandas/data/csv/artwork_data.pickle'
df_completo.to_pickle(path_guardado)

# leer pickle:
df_completo_pickle = pd.read_pickle(path_guardado)

#¿Cuantos datos tenemos?
df_completo.shape #--> 69 201 registros








