import scrapy
from ..items import FilmeItem

class ScraperfilmowSpider(scrapy.Spider):
    name = 'scraperfilmow'
    start_urls = ['https://filmow.com/filmes-todos/']
    
    custom_settings = {
        'DOWNLOAD_DELAY': 0.25,
        'LOG_FILE': 'filmow.log',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'result-filme.json'
    }

    def parse(self, response):
        links_filmes = response.css('#movies-list li span a:nth-child(2)::attr(href)').getall()
        for filme in links_filmes:
            url_filme = response.urljoin(filme)
            yield scrapy.Request(url_filme, callback=self.get_filme)
        proxima_pagina = response.css('a#next-page::attr(href)').get()
        if proxima_pagina is not None:
            url_proxima = response.urljoin(proxima_pagina)
            yield scrapy.Request(url_proxima)
        
    
    def get_filme(self, response):
        filme = FilmeItem()
        filme['titulo'] = response.css('div.movie-title h1::text').get()
        filme['titulo_original'] = response.css('h2.movie-original-title::text').get()
        filme['ano'] = response.css('div.span6 div:nth-child(1) small::text').get()
        filme['elenco'] = response.css('#casting li a span strong::text').getall()
        filme['media_geral'] = response.css('div.movie-rating-average span.average::text').get()
        filme['qtd_votos'] = response.css('div.movie-rating-wrapper div.summary span::text').get()
        yield filme
