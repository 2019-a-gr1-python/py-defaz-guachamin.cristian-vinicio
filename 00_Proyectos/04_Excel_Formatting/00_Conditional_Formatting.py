import pandas as pd

path_pickle = 'C:/Users/LeAdm/Documents/GitHub/py-defaz-guachamin.cristian-vinicio/00_Proyectos/04_Excel_Formatting' \
              '/vgsales.pickle'
df_completo_pickle = pd.read_pickle(path_pickle)
df = df_completo_pickle.iloc[0:999, :].copy()

# %% Ejercicio 1}
# Total de juegos desarrollados
juegos_contados = df_completo_pickle.groupby(['Name'])['Name'].agg(['count']) \
    .sort_values(by='count', ascending=False)
writer1 = pd.ExcelWriter('Numero_de_Juegos.xlsx', engine='xlsxwriter')
juegos_contados.to_excel(writer1, sheet_name="Numero de juegos")
hoja_numJuegos = writer1.sheets['Numero de juegos']
rango_celdas = 'B2:B{}'.format(len(juegos_contados) + 1)
formato_1 = {
    'type': '3_color_scale',
    'min_value': '10',
    'min_type': 'percentile',
    'max_value': '99',
    'max_type': 'percentile'
}
hoja_numJuegos.conditional_format(rango_celdas, formato_1)
writer1.save()

# %% Ejercicio 2
# Total de juegos de acción por año
df_completo_pickle = pd.read_pickle(path_pickle)
df_completo_pickle.set_index('Genre', inplace=True)
juegos_X_anio = df_completo_pickle.loc[['Action'], ['Year']].groupby(['Year'])['Year'].agg(['count']) \
    .sort_values(by='count', ascending=False)
writer2 = pd.ExcelWriter('Numero_Juegos_anio.xlsx', engine='xlsxwriter')
juegos_X_anio.to_excel(writer2, sheet_name="Juegos de accion por anio")
hoja_juegosXanio = writer2.sheets['Juegos de accion por anio']
rango_celdas2 = 'B2:B{}'.format(len(juegos_X_anio) + 1)
formato_2 = {
    'type': '3_color_scale',
    'min_value': '10',
    'min_type': 'percentile',
    'max_value': '99',
    'max_type': 'percentile'
}
hoja_juegosXanio.conditional_format(rango_celdas2, formato_2)
writer2.save()

# %% Ejercicio 3
# Numero de juegos desarrollados por Electronic Arts por Plataforma
df_completo_pickle = pd.read_pickle(path_pickle)
df_completo_pickle.set_index('Publisher', inplace=True)
juegos_por_plataforma = df_completo_pickle.loc[['Electronic Arts'], ['Platform']].groupby(['Platform'])['Platform'] \
    .agg(['count']).sort_values(by='count', ascending=False)
writer3 = pd.ExcelWriter('Juegos_por_plataforma.xlsx', engine='xlsxwriter')
juegos_por_plataforma.to_excel(writer3, sheet_name="Juegos por plataforma")
hoja_juegosXplataforma = writer3.sheets['Juegos por plataforma']
rango_celdas3 = 'B2:B{}'.format(len(juegos_por_plataforma) + 1)
formato_3 = {
    'type': 'data_bar',
    'bar_color': '#b4ff33'
}
hoja_juegosXplataforma.conditional_format(rango_celdas3, formato_3)
writer3.save()

# %% Ejercicio 4
# Monto total de ventas de videojuegos en Japon y EU (en miles de millones)
df_completo_pickle = pd.read_pickle(path_pickle)
ventas_EU = df_completo_pickle.groupby(['Name'])['EU_Sales'].agg(['sum']) \
    .sort_values(by='sum', ascending=False)
ventas_JP = df_completo_pickle.groupby(['Name'])['JP_Sales'].agg(['sum']) \
    .sort_values(by='sum', ascending=False)
writer4 = pd.ExcelWriter('Ventas_totales_EU_JP.xlsx', engine='xlsxwriter')
ventas_EU.to_excel(writer4, sheet_name="Ventas en EEUU")
ventas_JP.to_excel(writer4, sheet_name="Ventas en Japon")
hoja_EU = writer4.sheets['Ventas en EEUU']
hoja_JP = writer4.sheets['Ventas en Japon']
rango_celdasEU = 'B2:B{}'.format(len(ventas_EU) + 1)
rango_celdasJP = 'B2:B{}'.format(len(ventas_JP) + 1)
formato_4 = {'type': 'icon_set',
             'icon_style': '3_traffic_lights'}
hoja_EU.conditional_format(rango_celdasEU, formato_4)
hoja_JP.conditional_format(rango_celdasJP, formato_4)
writer4.save()

# %% Ejercicio 5
# Los 100 juegos más vendidos a nivel global.
df_completo_pickle = pd.read_pickle(path_pickle)
ventas_globales = df_completo_pickle.groupby(['Name'])['Global_Sales'].agg(['sum']) \
    .sort_values(by='sum', ascending=False).head(100)
writer5 = pd.ExcelWriter('100_mas_vendidos.xlsx', engine='xlsxwriter')
ventas_globales.to_excel(writer5, sheet_name="Ventas Gloables")
hoja_global = writer5.sheets['Ventas Gloables']
rango_celdasGlobales = 'B2:B{}'.format(len(ventas_globales) + 1)
formato_5 = {'type': 'icon_set',
             'icon_style': '3_arrows',
             'icons': [{'criteria': '>=', 'type': 'number', 'value': 50.0},
                       {'criteria': '<', 'type': 'number', 'value': 30.0},
                       {'criteria': '<=', 'type': 'number', 'value': 20.0}]
             }
hoja_global.conditional_format(rango_celdasGlobales, formato_5)
writer5.save()
