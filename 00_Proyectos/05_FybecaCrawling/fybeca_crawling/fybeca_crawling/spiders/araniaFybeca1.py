import scrapy
from fybeca_crawling.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


# 1) Generar URLS
def generar_urls():
    url_inicial = 'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=NUM&pp=25'
    urls = []
    for i in range(0, 151, 25):
        urls.append(url_inicial.replace('NUM', str(i)))
    return urls


class AraniaFybeca1(scrapy.Spider):
    name = 'arania_fybeca1'

    def start_requests(self):
        for url in generar_urls():
            yield scrapy.Request(url=url)

    def parse(self, response):
        productos = response.css('div.product-tile-inner')
        for producto in productos:
            existe_producto = len(producto.css('div.detail'))
            if existe_producto > 0:
                # Verificar si existe producto:
                producto_loader = ItemLoader(
                    item=ProductoFybeca(),
                    selector=producto
                )
                # Llenar los datos del producto loader
                # Anadir el precio (clase, input, output)
                producto_loader.add_css(
                    'precio',
                    '.price::attr(data-bind)'
                )

                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                )
                producto_loader.default_output_processor = TakeFirst()

                """
                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                )
                
                """

                # producto_imprimir = producto_loader.load_item()
                # print(producto_imprimir)
                yield producto_loader.load_item()
