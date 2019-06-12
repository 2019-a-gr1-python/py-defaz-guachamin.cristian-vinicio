import pandas as pd
import os
import sqlite3
import numpy as np

path_guardado = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/03_Pandas/data/csv/' \
                'artwork_data.pickle'
df_completo_pickle = pd.read_pickle(path_guardado)
df = df_completo_pickle.iloc[49980:50019, :].copy()

"""
Tipos de archivo:
- JSON
- SQL
. EXCEL
"""

# ============================= EXCEL =============================
df.to_excel('ejemplo_basico.xlsx')

# Sin índices:
df.to_excel('ejemplo_basico_sin_indices.xlsx', index=False)

# Utilizar solo algunas columnas
columnas = ['artist', 'title', 'year']
df.to_excel('columnas.xlsx', columns=columnas)

# Múltiples hojas de trabajo (worksheet)
writer = pd.ExcelWriter('multiples_worksheet.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Preview')
df.to_excel(writer, sheet_name='Preview Dos', index=False)
df.to_excel(writer, sheet_name='Preview Tres', columns=columnas)
writer.save()

# Formateo Condicional
artistas_contados = df_completo_pickle['artist'].value_counts()
writer = pd.ExcelWriter('clores.xlsx', engine='xlsxwriter')
artistas_contados.to_excel(writer, sheet_name='Artistas contados')
hoja_artistas = writer.sheets['Artistas contados']
rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)

formato = {
    'type': '2_color_scale',
    'min_value': '10',
    'min_type': 'percentile',
    'max_value': '99',
    'max_type': 'percentile'
}

hoja_artistas.conditional_format(rango_celdas, formato)
writer.save()

# ============================= SQLite =============================
with sqlite3.connect('bdd_python.db') as conexion:
    df.to_sql('tabla', conexion)


# ============================== JSON =============================
df.to_json('artistas.json')
df.to_json('artistas_orientado_tabla.json', orient='table')

# #################################
# Ejercicios Excel, Conditional formatting:
writer1 = pd.ExcelWriter('ejemplo1.xlsx', engine='xlsxwriter')
df.to_excel(writer1, sheet_name='Artistas por anio')
hoja_anios = writer1.sheets['Artistas por anio']

# Completar para el miercoles próximo::::






