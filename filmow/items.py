# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmeItem(scrapy.Item):
    # define the fields for your item here like:
    titulo = scrapy.Field()
    titulo_original = scrapy.Field()
    ano = scrapy.Field()
    elenco = scrapy.Field()
    # sinopse = scrapy.Field()
    media_geral = scrapy.Field()
    qtd_votos = scrapy.Field()


class SerieItem(scrapy.Item):
    # define the fields for your item here like:
    titulo = scrapy.Field()


class DiretorItem(scrapy.Item):
    # define the fields for your item here like:
    nome = scrapy.Field()
    
