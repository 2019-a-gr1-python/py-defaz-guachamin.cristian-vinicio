# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import re

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def transformar_url_imagen(texto):
    url = 'https://www.fybeca.com'
    cadena_a_reemplazar = '../..'
    print('ASDASDAS')
    return texto.replace(cadena_a_reemplazar, url)


# 3) Transformar el precio a numero (float)
def obtener_precio_item(precio):
    regex = r"(\d+\.\d{1,})"
    return float(re.search(regex, precio).group(0))


class ProductoFybeca(scrapy.Item):
    # 2) Añadir el precio (clase, input, output)
    precio = scrapy.Field(
        input_processor=MapCompose(
            obtener_precio_item
        ),
        output_processor=TakeFirst()
    )
    titulo = scrapy.Field()
    """
     imagen = scrapy.Field(
        input_processor=MapCompose(transformar_url_imagen),
        output_processor=TakeFirst()
    )
    titulo = scrapy.Field()

    """

