import pandas as pd
import re

# import numpy as np

# Cargando excel
df_inicial = pd.read_excel('E:/00_python/INFORMACIÓN-GENERAL.xlsx', sheet_name='Bodega1')

# %% Columna NombreBodega
# Eliminando impurezas y espacios vacios entre palabras
col_nom_bodega = df_inicial['BODEGA']
type(col_nom_bodega)
arrgelo_nombres = col_nom_bodega.values
type(arrgelo_nombres)


# Funcion para depurar
def depurar(arreglo_con_impurezas):
    arreglo_depurado = []
    for i in range(0, len(arreglo_con_impurezas)):
        arreglo_depurado.append(
            re.sub('\r?\n', ' ', arreglo_con_impurezas[i]
                   .replace('\n', ' ')
                   .replace(u'\xa0', u'')
                   .replace('  ', ' ').strip()))
    return arreglo_depurado


arrgelo_nombres_depurado = depurar(arrgelo_nombres)
# Creando dataframe con datos depurados
df_final = pd.DataFrame(arrgelo_nombres_depurado, columns=['Nombre'])

# %% Columna CódigoBodega
col_codigo_bodega = df_inicial['CÓDIGO DE BODEGA']
arr_codigo = col_codigo_bodega.values
arr_codigo_depuraado = depurar(arr_codigo)
# Agrgando nueva columna
df_final['Codigo'] = arr_codigo_depuraado

# %% Columna Direccion
col_direccion = df_inicial['DIRECCION ']
arr_direccion = col_direccion.values
arr_direccion_depurado = depurar(arr_direccion)
df_final['direccion'] = arr_direccion_depurado

# %% Columna Administrador
col_admin = df_inicial['ADMINISTRADOR']
arr_admin = col_admin.values
arr_admin_depuraado = depurar(arr_admin)
df_final['Administrador'] = arr_admin_depuraado


# %% Columna correo electrónico
col_correo = df_inicial['CORREO ELECTRÓNICO']
arr_correo = col_correo.values
arr_correo_depurado = depurar(arr_correo)


def validar_correo(lista_correos):
    lista_correos_dep = []
    reg = '^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$'
    for correo in lista_correos:
        if re.match(reg, correo.lower()):
            lista_correos_dep.append(correo)
        else:
            lista_correos_dep.append('')
    return lista_correos_dep


arr_correo_depurado_dos = validar_correo(arr_correo_depurado)
df_final['Correo electronico'] = arr_correo_depurado_dos

# %% Columa telefono
col_telf = df_inicial['TELÉFONO'].fillna('').astype(str)
arr_telf = col_telf.values
arr_telf_depurado = depurar(arr_telf)
arr_telf_limpio = []
# Eliminando ceros
for t in arr_telf_depurado:
    arr_telf_limpio.append(t[:-2])

df_final['telefono'] = arr_telf_limpio

# %% Columna extensiones
col_ext = df_inicial['EXT.'].fillna('').astype(str)
arr_ext = col_ext.values
arr_ext_depurado = depurar(arr_ext)
df_final['Ext.'] = arr_ext_depurado

# %% Columna celulares
col_cel = df_inicial['CELULAR'].fillna('').astype(str)
arr_cel = col_cel.values
arr_cel_depurado = depurar(arr_cel)
arr_cel_limpio = []

# Eliminando ceros
for t in arr_cel_depurado:
    arr_cel_limpio.append(t[:-2])


# Agregando ceros si faltan:
def completar_ceros(arr_celulares):
    arr_cel_completo = []
    for cel in arr_celulares:
        if len(cel) == 9:
            arr_cel_completo.append('0'+cel)
        else:
            arr_cel_completo.append(cel)
    return arr_cel_completo


arr_cel_final = completar_ceros(arr_cel_limpio)
df_final['celular'] = arr_cel_final

# %% Columnas latitud y longitud
lista_coordenadas = ['-0.188499,-76.640800', '0.084381,-76.880142', '-0.338010,-77.808418',
                     '-0.449061,-77.874213', '-0.290281,-78.539498', '-0.290281,-78.539498',
                     '-0.270341,-78.528773', '-0.270341,-78.528773', '-0.270951,-79.098748',
                     '0.988754,-79.647310', '0.900209,-79.706976', '-2.035250,-80.004435',
                     '-2.231445,-80.899080', '-2.040921,-80.723390']
arreglo_latitud = []
arreglo_longitud = []
for x in lista_coordenadas:
    coord = x.split(',')
    arreglo_latitud.append(coord[0])
    arreglo_longitud.append(coord[1])

df_final['Latitud direccion'] = arreglo_latitud
df_final['Longitud direccion'] = arreglo_longitud

# %% Dataframe al excel:
# writer = pd.ExcelWriter('bodegas-py.xlsx', engine='xlsxwriter')
df_final.to_excel('E:/00_python/bodegas-py.xlsx', index=False)

