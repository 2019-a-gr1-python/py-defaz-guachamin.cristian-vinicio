# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import MapCompose, TakeFirst


def convertir_a_entero(disco_rank):
    return int(disco_rank)


def obtener_flotante(drive_value):
    regex = r"(\d+\.\d{1,})"
    if drive_value == 'NA':
        return 0.0
    else:
        return float(re.search(regex, drive_value).group(0))


def obtener_precio(price):
    regex = r"(\d+\.\d{1,})"
    clean_price = price.replace('$', '').replace('*', '')
    if clean_price == 'NA':
        return 0.0
    else:
        return float(re.search(regex, clean_price).group(0))


class BenchmarkingItemHDD(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nombre_hdd = scrapy.Field()

    disco_rating = scrapy.Field(
        input_processor=MapCompose(
            convertir_a_entero
        ),
        output_processor=TakeFirst()
    )
    disco_rank = scrapy.Field(
        input_processor=MapCompose(
            convertir_a_entero
        ),
        output_processor=TakeFirst()
    )
    drive_value = scrapy.Field(
        input_processor=MapCompose(
            obtener_flotante
        ),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(
            obtener_precio
        ),
        output_processor=TakeFirst()
    )


class BenchmarkingItemGPU(scrapy.Item):

    nombre_vc = scrapy.Field()

    passmark_rank = scrapy.Field(
        input_processor=MapCompose(
            convertir_a_entero
        ),
        output_processor=TakeFirst()
    )
    videocard_rank = scrapy.Field(
        input_processor=MapCompose(
            convertir_a_entero
        ),
        output_processor=TakeFirst()
    )
    videocard_value = scrapy.Field(
        input_processor=MapCompose(
            obtener_flotante
        ),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(
            obtener_precio
        ),
        output_processor=TakeFirst()
    )


class BenchmarkingItemRAM(scrapy.Item):
    memory_name = scrapy.Field()

    latency = scrapy.Field(
        input_processor=MapCompose(
            convertir_a_entero
        ),
        output_processor=TakeFirst()
    )
    read_uncached = scrapy.Field(
        input_processor=MapCompose(
            convertir_a_entero
        ),
        output_processor=TakeFirst()
    )
    write_speed = scrapy.Field(
        input_processor=MapCompose(
            convertir_a_entero
        ),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(
            obtener_precio
        ),
        output_processor=TakeFirst()
    )


class BenchmarkingItemCPU(scrapy.Item):
    cpu_name = scrapy.Field()

    passmark_rank = scrapy.Field(
        input_processor=MapCompose(
            convertir_a_entero
        ),
        output_processor=TakeFirst()
    )
    cpu_rank = scrapy.Field(
        input_processor=MapCompose(
            convertir_a_entero
        ),
        output_processor=TakeFirst()
    )
    cpu_value = scrapy.Field(
        input_processor=MapCompose(
            obtener_flotante
        ),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(
            obtener_precio
        ),
        output_processor=TakeFirst()
    )


class BenchmarkingItemDesktop(scrapy.Item):
    col0 = scrapy.Field()
    col1 = scrapy.Field()
    col2 = scrapy.Field()
    col3 = scrapy.Field()
    col4 = scrapy.Field()
    col5 = scrapy.Field()
    col6 = scrapy.Field()
    col7 = scrapy.Field()
    col8 = scrapy.Field()
    col9 = scrapy.Field()
    col10 = scrapy.Field()
