# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pandas as pd


class FiltrarSoloTabletas(object):

    @staticmethod
    def process_item(item, spider):
        # Estas clases deben tener una funcion que diga process-item, sino, no servirá.
        # Buscar palabra que diga 'capsula' en una cadena
        titulo = item['titulo']
        print(titulo)
        if 'capsula' not in titulo:
            raise DropItem('No tiene cápsula en el título')
        else:
            return item


class TransformarTituloAMinusculas(object):
    @staticmethod
    def process_item(item, spider):
        print(item['titulo'])
        item['titulo'] = item['titulo'].lower()
        return item


def calcular_promedio():
    df = pd.read_csv('tmp/ListaPreciosFybeca.csv')
    df.head()
    return df.precio.mean()


# 5) Añadir un pipeline para seleccionar los productos mayores al precio promedio
class ObtenerProductosMayoresAlPromedio(object):
    @staticmethod
    def process_item(item, spider):
        promedio = calcular_promedio()
        print(f'Promedio de precios: {promedio}')
        if item['precio'] > promedio:
            return item
        else:
            raise DropItem('Producto con precio menor al promedio')
