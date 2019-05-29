import pandas as pd

path = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/03_Pandas/data/artwork'
archivo = '/a/000/a00001-1035.json'
path_guardado = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/03_Pandas/data/csv/artwork_data.pickle'
df_completo_pickle = pd.read_pickle(path_guardado)

# Sacar columna dento de dataframe
serie_artistas_duplicados = df_completo_pickle['artist']

artistas = pd.unique(serie_artistas_duplicados)

print(artistas.size())
print(len(artistas))

blake = df_completo_pickle['artist'] == 'Bñake, William'
print(df_completo_pickle[blake])
