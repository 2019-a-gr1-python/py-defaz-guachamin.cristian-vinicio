from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_03.items import ProductoFybeca


class AraniaFybeca(CrawlSpider):
    name = 'crawl_fybeca1'  # Heredado (conservar nombre)
    allowed_domains = [  # Heredado (conservar nombre)
        'fybeca.com'
    ]
    start_urls = [  # Heredado (conservar nombre)
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25'

        # esults.jsf?s=25&pp=25&cat=238&b=-1&ot=0
        # -results.jsf?s=50&pp=25&cat=238&b=-1&ot=0
        # h-results.jsf?s=0&pp=25&cat=238&b=-1&ot=0
    ]
    # Heredado (conservar nombre)
    url_segmento_permitido = (
        'FybecaWeb/pages/search-results.jsf?cat=238'
    )

    rules = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido
            ), callback='parse'),
    )

    def parse(self, response):

        productos = response.css('div.product-tile-inner')
        for producto in productos:
            existe_producto = len(producto.css('div.detail'))
            # Verificar si existe producto:
            if existe_producto > 0:
                producto_loader = ItemLoader(
                    item=ProductoFybeca(),
                    selector=producto
                )
                # Llenar los datos del producto loader
                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                )
                producto_loader.default_output_processor = TakeFirst()
                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                )

                # producto_imprimir = producto_loader.load_item()
                # print(producto_imprimir)
                yield producto_loader.load_item()
