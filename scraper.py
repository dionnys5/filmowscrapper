from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from filmow.spiders.scraperfilmow import ScraperfilmowSpider

settings = get_project_settings()
# settings.set('FEED_FORMAT', 'csv')
# Aqui os settings do projeto são importados para o processo
process = CrawlerProcess(settings)
# O processo recebe a spider que deve realizar a extração
process.crawl(ScraperfilmowSpider)
# O Script vai ficar bloqueado aqui até que o spider tenha finalizado a coleta de dados
process.start()