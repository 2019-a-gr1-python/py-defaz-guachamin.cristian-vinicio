import pandas as pd
import numpy as np

path = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/03_Pandas/data/artwork'
archivo = '/a/000/a00001-1035.json'
path_guardado = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/03_Pandas/data/csv/artwork_data.pickle'
df_completo_pickle = pd.read_pickle(path_guardado)

# Sacar columna dento de dataframe
serie_artistas_duplicados = df_completo_pickle['artist']

artistas = pd.unique(serie_artistas_duplicados)

print(artistas.size())
print(len(artistas))

blake = df_completo_pickle['artist'] == 'Blake, William'
print(df_completo_pickle[blake])

arr = np.array([1, 2, 3])
arr2 = arr.reshape()
