# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:33:49 2019
@author: LeAdm
"""
import json
import pandas as pd
import os

# %%
path = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/03_Pandas/data/artwork'
pathMac = '/Users/usrdel/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/03_Pandas/data/artwork'

archivo = '/a/000/a00001-1035.json'

# %%

path_archivo = path + archivo

llaves = ['id', 'all_artists', 'title', 'medium',
          'dateText', 'acquisitionYear',
          'height', 'width', 'units']

# registro = [[1, 2, 3, 4, 4, 5, 56, 7, 8, 9, 0]]

# %%
"""
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
"""


# transformar a una funcion:
def leer_json(path_archivo1, llaves1):
    with open(path_archivo1) as text_json:
        contenido_json = json.load(text_json)
    registro_df_lista = []
    for llave in llaves1:
        valor = contenido_json[llave]
        registro_df_lista.append(valor)
    return registro_df_lista


leer_json(path_archivo, llaves)
# %%


def leer_json_en_carpetas(directorio, llaves1):  # Leer json en carpetas
    trabajos_arte = []
    print(type(os.walk(directorio)))  #
    for path_raiz, lista_directorios, archivos in os.walk(directorio):
        print(path_raiz)
        print(type(path_raiz))  # String -> Path Actual
        print(lista_directorios)
        print(type(lista_directorios))  # List String directorios
        print(archivos)
        print(type(archivos))  # List Strings nombre archivos
        for nombre_archivo in archivos:
            print(nombre_archivo)
            if nombre_archivo.endswith('json'):
                directorio_archivo = os.path.join(
                    path_raiz,
                    nombre_archivo
                )
                pieza_arte = leer_json(directorio_archivo, llaves1)
                trabajos_arte.append(pieza_arte)

    df = pd.DataFrame.from_records(
        trabajos_arte,
        columns=llaves1,
        index='id'
    )
    return df

# %% Leer mùltiples json:

df_artworks = leer_json_en_carpetas(path, llaves)
