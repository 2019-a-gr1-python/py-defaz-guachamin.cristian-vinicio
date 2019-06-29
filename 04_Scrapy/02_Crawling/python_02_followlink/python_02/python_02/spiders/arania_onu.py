import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class AraniaCrawlOnu(CrawlSpider):
    name = 'crwal_onu'  # Heredado (conservar nombre)
    allowed_domains = [  # Heredado (conservar nombre)
        'un.org'
    ]
    start_urls = [  # Heredado (conservar nombre)
        'http://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]
    # Heredado (conservar nombre)
    url_segmento_permitido = (
        'funds-programmes-specialized-agencies-and-others'
    )
    url_segmento_retringido = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )

    regla_uno = (
        Rule(
            LinkExtractor(), callback='parse_page')
        ,
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido
            ), callback='parse_page')
        ,
    )
    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido,
                deny=url_segmento_retringido
            ), callback='parse_page')
        ,
    )

    rules = regla_tres

    def parse_page(self, response):
        lista_programas = response.css('div.field-items > div.field-item > h4::text').extract()
        # iterar ista y guardar en archivos
        for agencia in lista_programas:
            with open('onu_agencias.txt', 'a+') as archivo:
                archivo.write(agencia + '\n')
