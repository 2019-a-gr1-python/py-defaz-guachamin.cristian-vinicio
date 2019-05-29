# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:33:49 2019

@author: LeAdm
"""
import json
import pandas as pd
import os

path = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/03_Pandas/data/artwork'
archivo = '/a/000/a00001-1035.json'

# with: se encarga de cerrar automáticamente el archivo.
path_archivo = path + archivo

llaves = ['id','all_artist','title','medium',
          'dateText','acquisitionYear',
          'height','width','units']
registro = [[1,2,3,4,4,5,56,7,8,9,0]]

#%%


with open(path_archivo) as text_json:
    contenido_json = json.load(text_json)
    print(contenido_json)
    print(type(contenido_json))
# La carga de memoria será considerable al utilizar json como diccionarios
    registro_df_lista = []
    for llave in llaves:
        valor = contenido_json[llave]
        registro_df_lista.append(valor)
    registro_df_tupla = tuple(registro_df_lista)

print(registro_df_tupla)
# se pueden usar listas o tupla para crear dataframes
df_chiquito = pd.DataFrame([registro_df_lista])
df_chiquito_t = pd.DataFrame([registro_df_tupla])

# transformar a una funcion:
def leer_json(path_archivo,llaves):
    with open(path_archivo) as text_json:
        contenido_json = json.load(text_json)
    registro_df_lista = []
    for llave in llaves:
        valor = contenido_json[llave]
        registro_df_lista.append(valor)
    return registro_df_lista

leer_json(path_archivo,llaves)


