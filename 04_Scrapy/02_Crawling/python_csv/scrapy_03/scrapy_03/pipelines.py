from scrapy.exceptions import DropItem


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


class TransformarTituloAMinuscualas(object):
    @staticmethod
    def process_item(item, spider):
        print(item['titulo'])
        item['titulo'] = item['titulo'].lower()
        return item
