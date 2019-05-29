import pandas as pd

path_guardado = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/03_Pandas/data/csv/artwork_data.pickle'
df = pd.read_pickle(path_guardado)

# primero = df.loc[1035]  # error, no esta en el índice
# loc: filtra por label
primero = df.loc[1035, 'artist']
segundo = df.loc[1036, 'units']

# df.loc[0] # Error porque no esta dentro del label indice
# filtrar por nombre o filtra por entero, ambos ayudan.
# iloc: filtra por posición
primero_a = df.iloc[0, 1]
# iloc con rangos de cosas:
primero_b = df.iloc[0, :]
primero_c = df.iloc[0:100, 2:4]

# slice:
tres_primeros = df.head(10)['width'].sort_values(ascending = False).head(3)
tres_ultimos = df.head(10)['width'].sort_values().tail(3)

a = df['year'].sort_values(axis=0)

serie_validado =  pd.to_numeric(df['width'], errors = 'coerce')

# arreglando dataframe

df.loc[::,'width'] = serie_validado
df.iloc[:,5] = serie_validado

# escoger los que mas y menos 'wodth' tienen:
diez_primeros = df['width'].sort_values(ascending = False).head(10)
diez_ultimos = df['width'].sort_values(ascending = False).tail(10)

# calcular el área de una obra de arte:
# widht * height, pero height aun no esta validado, entonces:
serie_validado_height = pd.to_numeric(df['height'], errors = 'coerce')
df.loc[:,'height'] = serie_validado_height

# hallando área
area = df['height'] * df['width']
type(area) # es una serie ya multiplicada

df['area'] = 0 # crea la columna parea en dataframe df
df['area'] = area  # asigna datos
df = df.assign(areados = area)

# obtener el que tiene mayor área tiene
df_area = df['area'].sort_values(ascending = False).head(1)
# maximo y minimo valor más rápido:
id_max_area = df['area'].idxmax() # índice: label 
id_min_area = df['area'].idxmin() # indice: label
# obtener el registro más alto (serie), fila completa
registro_mas_area = df.loc[id_max_area]
registro_menor_area = df.loc[id_min_area]

