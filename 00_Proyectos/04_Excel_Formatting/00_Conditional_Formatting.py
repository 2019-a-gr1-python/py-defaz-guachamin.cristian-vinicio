import pandas as pd

path_pickle = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/00_Proyectos/04_Excel_Formatting' \
              '/vgsales.pickle'
df_completo_pickle = pd.read_pickle(path_pickle)
df = df_completo_pickle.iloc[0:999, :].copy()

# %% Ejercicio 1
juegos_contados = df_completo_pickle.groupby(['Name'])['Name'].agg(['count'])\
    .sort_values(by='count', ascending=False)
writer1 = pd.ExcelWriter('Numero_de_Juegos.xlsx', engine='xlsxwriter')
juegos_contados.to_excel(writer1, sheet_name="Numero de juegos")
hoja_numJuegos = writer1.sheets['Numero de juegos']
rango_celdas = 'B2:B{}'.format(len(juegos_contados)+1)
formatoDatos = {
    'type': '3_color_scale',
    'min_value': '10',
    'min_type': 'percentile',
    'max_value': '99',
    'max_type': 'percentile'
}
hoja_numJuegos.conditional_format(rango_celdas, formatoDatos)
writer1.save()

# %% Ejercicio 2
df_completo_pickle = pd.read_pickle(path_pickle)
df_completo_pickle.set_index('Genre', inplace=True)
juegos_X_anio = df_completo_pickle.loc[['Action'], ['Year']].groupby(['Year'])['Year'].agg(['count'])\
    .sort_values(by='count', ascending=False)
writer2 = pd.ExcelWriter('Numero_Juegos_anio.xlsx', engine='xlsxwriter')
juegos_X_anio.to_excel(writer2, sheet_name="Juegos de accion por anio")
hoja_juegosXanio = writer2.sheets['Juegos de accion por anio']
rango_celdas2 = 'B2:B{}'.format(len(juegos_X_anio)+1)
hoja_juegosXanio.conditional_format(rango_celdas2, formatoDatos)
writer2.save()

# %% Ejercicio 3
