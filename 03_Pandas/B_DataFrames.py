# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:37:11 2019

@author: LeAdm
"""

import numpy as np
import pandas as pd

arr_rand = np.random.randint(0,10,6).reshape(2,3)

df = pd.DataFrame(arr_rand)

# poniendo nombres a las columnas
df1 = pd.DataFrame(
        arr_rand,
        columns=['Estatura (cm)','Peso (gr)','Edad (anios)'],
        index=['Criss','Vinicio']
        )



df2 = pd.DataFrame(
        arr_rand
        )
# Colocar columnas eindices
df2.columns = ['Estatura (cm)','Peso (gr)','Edad (anios)']
df2.index = ['Criss','Vinicio']

df3 = pd.DataFrame(
        arr_rand
        )
df3[0] # No es el índice
df2['Estatura (cm)'] # Es el nombre de la columna
type(df2['Estatura (cm)']) #Es una serie :: Dataframe: conjunto de series

df2['Estatura (cm)'][0]

