import scrapy


class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    libros = ""

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url)

    def parse(self, response):  # self = this, response
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css('h3 > a::attr(title)').extract()
        stocks = etiqueta_contenedora.css('div.product_price > p.instock.availability::text').extract()
        precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        print(titulos)
        print(stocks)
        print(precios)
        # Guardando en un arrglo o un diccionario
        lista_titulos = ''
        for titulo in titulos:
            lista_titulos += titulo + '\n'

        lista_stocks = ''
        for stock in stocks:
            lista_stocks += stock + '\n'

        lista_precios = ''
        for precio in precios:
            lista_precios += precio + '\n'

        archivo_libros = open("./libros.txt", mode='a')
        archivo_libros.write(lista_titulos + '\n' + lista_precios + '\n' + lista_stocks)
        archivo_libros.close()
