from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class AraniaBooks(CrawlSpider):
    name = 'crawl_books'  # Heredado (conservar nombre)
    allowed_domains = [  # Heredado (conservar nombre)
        'toscrape.com'
    ]
    start_urls = [  # Heredado (conservar nombre)

        'http://books.toscrape.com/index.html'
    ]
    # Heredado (conservar nombre)
    url_segmento_permitido = (
        'category/books/mystery_3',
        'category/books/fantasy_19'
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido
            ), callback='parse_page'),
    )

    rules = regla_dos

    @staticmethod
    def parse_page(response):
        lista_libros = response.css('article.product_pod > h3 > a::attr(title)').extract()
        # iterar ista y guardar en archivos
        for libro in lista_libros:
            with open('misterio_fantasia.txt', 'a+') as archivo1:
                archivo1.write(libro + '\n')
