import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from benchmarking.items import BenchmarkingItemHDD, BenchmarkingItemGPU, BenchmarkingItemCPU, BenchmarkingItemRAM, \
    BenchmarkingItemDesktop


# Hard Drive
class AraniaBenchmarkHDD(scrapy.Spider):
    name = 'arania_benchmarkHDD'

    def parse(self, response):

        tb = response.xpath('//table')
        for td in tb.xpath('.//tbody/tr'):
            producto_loader = ItemLoader(item=BenchmarkingItemHDD(), selector=td)
            producto_loader.add_xpath(
                'nombre_hdd',
                './/td[1]/a/text()'
            )
            producto_loader.add_xpath(
                'disco_rating',
                # '(.//td[2]/text())[position()>6]'
                './/td[2]/text()'
            )
            producto_loader.add_xpath(
                'disco_rank',
                './/td[3]/text()'
            )
            producto_loader.add_xpath(
                'drive_value',
                './/td[4]/text() | .//td[4]/a/text()'
            )
            producto_loader.add_xpath(
                'price',
                './/td[5]/text() | .//td[5]/a/text()'
            )
            producto_loader.default_output_processor = TakeFirst()
            yield producto_loader.load_item()

    def start_requests(self):
        urls = [
            'https://www.harddrivebenchmark.net/hdd_list.php'
        ]
        for url in urls:
            yield scrapy.Request(url=url)


# VideoCard
class AraniaBenchmarkGPU(scrapy.Spider):
    name = 'arania_benchmarKGPU'

    def parse(self, response):

        tb = response.xpath('//table')
        for td in tb.xpath('.//tbody/tr'):
            producto_loader = ItemLoader(item=BenchmarkingItemGPU(), selector=td)
            producto_loader.add_xpath(
                'nombre_vc',
                './/td[1]/a/text()'
            )
            producto_loader.add_xpath(
                'passmark_rank',
                './/td[2]/text()'
            )
            producto_loader.add_xpath(
                'videocard_rank',
                './/td[3]/text()'
            )
            producto_loader.add_xpath(
                'videocard_value',
                './/td[4]/text() | .//td[4]/a/text()'
            )
            producto_loader.add_xpath(
                'price',
                './/td[5]/text() | .//td[5]/a/text()'
            )
            producto_loader.default_output_processor = TakeFirst()
            yield producto_loader.load_item()

    def start_requests(self):
        urls = [
            'https://www.videocardbenchmark.net/gpu_list.php'
        ]
        for url in urls:
            yield scrapy.Request(url=url)


# Memory RAM
class AraniaBenchmarkRAM(scrapy.Spider):
    name = 'arania_benchmarkRAM'

    def parse(self, response):

        tb = response.xpath('//table')
        for td in tb.xpath('.//tbody/tr'):
            producto_loader = ItemLoader(item=BenchmarkingItemRAM(), selector=td)
            producto_loader.add_xpath(
                'memory_name',
                './/td[1]/a/text()'
            )
            producto_loader.add_xpath(
                'latency',
                './/td[2]/text()'
            )
            producto_loader.add_xpath(
                'read_uncached',
                './/td[3]/text()'
            )
            producto_loader.add_xpath(
                'write_speed',
                './/td[4]/text() | .//td[4]/a/text()'
            )
            producto_loader.add_xpath(
                'price',
                './/td[5]/text() | .//td[5]/a/text()'
            )
            producto_loader.default_output_processor = TakeFirst()
            yield producto_loader.load_item()

    def start_requests(self):
        urls = [
            'https://www.memorybenchmark.net/ram_list.php'
        ]
        for url in urls:
            yield scrapy.Request(url=url)


# Procesador
class AraniaBenchmarkCPU(scrapy.Spider):
    name = 'arania_benchmarkCPU'

    def parse(self, response):

        tb = response.xpath('//table')
        for td in tb.xpath('.//tbody/tr'):
            producto_loader = ItemLoader(item=BenchmarkingItemCPU(), selector=td)
            producto_loader.add_xpath(
                'cpu_name',
                './/td[1]/a/text()'
            )
            producto_loader.add_xpath(
                'passmark_rank',
                './/td[2]/text()'
            )
            producto_loader.add_xpath(
                'cpu_rank',
                './/td[3]/text()'
            )
            producto_loader.add_xpath(
                'cpu_value',
                './/td[4]/text() | .//td[4]/a/text()'
            )
            producto_loader.add_xpath(
                'price',
                './/td[5]/text() | .//td[5]/a/text()'
            )
            producto_loader.default_output_processor = TakeFirst()
            yield producto_loader.load_item()

    def start_requests(self):
        urls = [
            'https://www.cpubenchmark.net/cpu_list.php'
        ]
        for url in urls:
            yield scrapy.Request(url=url)


# Laptops, procesadores y servidores
class AraniaBenchmarkDesktop(scrapy.Spider):
    name = 'arania_benchmarkDesk'

    def parse(self, response):

        tb = response.xpath('//table')
        for td in tb.xpath('.//tr[contains(@bgcolor, "#FFFFFF")] | .//tr[contains(@bgcolor, "#EEEEEE")]'):
            producto_loader = ItemLoader(item=BenchmarkingItemDesktop(), selector=td)
            producto_loader.add_xpath(
                'col0',
                './/td[1]/text() | .//td[1]/b/font/text() | .//td[1]/a/text()'
            )
            producto_loader.add_xpath(
                'col1',
                './/td[2]/text() | .//td[2]/b/font/text() | .//td[2]/a/text()'
            )
            producto_loader.add_xpath(
                'col2',
                './/td[3]/text() | .//td[3]/b/font/text() | .//td[3]/a/text()'
            )
            producto_loader.add_xpath(
                'col3',
                './/td[4]/text() | .//td[4]/b/font/text() | .//td[4]/a/text()'
            )
            producto_loader.add_xpath(
                'col4',
                './/td[5]/text() | .//td[5]/b/font/text() | .//td[5]/a/text()'
            )
            producto_loader.add_xpath(
                'col5',
                './/td[6]/text() | .//td[6]/b/font/text() | .//td[6]/a/text()'
            )
            producto_loader.add_xpath(
                'col6',
                './/td[7]/text() | .//td[7]/b/font/text() | .//td[7]/a/text()'
            )
            producto_loader.add_xpath(
                'col7',
                './/td[8]/text() | .//td[8]/b/font/text() | .//td[8]/a/text()'
            )
            producto_loader.add_xpath(
                'col8',
                './/td[9]/text() | .//td[9]/b/font/text() | .//td[9]/a/text()'
            )
            producto_loader.add_xpath(
                'col9',
                './/td[10]/text() | .//td[10]/b/font/text() | .//td[10]/a/text()'
            )
            producto_loader.add_xpath(
                'col10',
                './/td[11]/text() | .//td[11]/b/font/text() | .//td[11]/a/text()'
            )

            producto_loader.default_output_processor = TakeFirst()
            yield producto_loader.load_item()

        # 'https://www.pcbenchmarks.net/fastest-desktop.html'
        # 'https://www.pcbenchmarks.net/fastest-laptop.html'
    def start_requests(self):
        urls = [
            'https://www.pcbenchmarks.net/fastest-server.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url)
