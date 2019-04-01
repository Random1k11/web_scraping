from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from dental.spiders.dental import DentalFirstSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(DentalFirstSpider)
process.start()
