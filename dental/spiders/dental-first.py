import scrapy
from dental.items import DentalItem
from bs4 import BeautifulSoup
import re


class DentalFirstSpider(scrapy.Spider):

    name = 'dental'
    start_urls = ['https://dental-first.ru/']


    def __init__(self):
        self.declare_xpath()


    def declare_xpath(self):
        self.main_menuXpath = '//div[@class="box-catalog-list"]/ul/li/a/@href'
        self.sub_menuXpath = "//ul[@class='bx_catalog_line_ul']/li/a/@href"
        self.itemsXpath = '//a[@class="bx_catalog_item_images"]/@href'
        self.TitleXpath  = "//h1[@itemprop='name']/text()"
        self.manyTitleXpath = "//div[@class='list_list_p']/span/text()"
        self.priceXpath = "//span[@itemprop='price']/text()"
        self.BrandXpath = "//table[@class='tabletable']"
        self.artikulXpath = "//table[@class='tabletable']"
        self.codelXpath = "//table[@class='tabletable']"
        self.countryXpath = "//table[@class='tabletable']"
        self.descriptionXpath = "//div[@class='bx_item_description']/text()"


    def parse(self, response):
        for url in response.xpath(self.main_menuXpath):
            url = 'https://dental-first.ru' + url.extract()
            yield scrapy.Request(url, callback=self.parse_sub_menu)


    def parse_sub_menu(self, response):
        for url in response.xpath(self.sub_menuXpath):
            url = 'https://dental-first.ru' + url.extract()
            yield scrapy.Request(url,  callback=self.parse_list_items)


    def parse_list_items(self, response):
        for url in response.xpath(self.sub_menuXpath):
            url = 'https://dental-first.ru' + url.extract()
            yield scrapy.Request(url, callback=self.parse_items)


    def parse_items(self, response):
        for url in response.xpath(self.itemsXpath):
            url = 'https://dental-first.ru' + url.extract()
            # print(url)
            yield scrapy.Request(url, callback=self.get_info_about_items)


    def get_info_about_items(self, response):

        try:
            Price = response.xpath(self.priceXpath).extract_first().strip()
        except AttributeError:
            print('Новый запрос')
            yield scrapy.Request(response.url, callback=self.parse_items)

        Title = response.xpath(self.TitleXpath).extract_first()
        Price = response.xpath(self.priceXpath).extract_first().strip()
        Brand = response.xpath(self.BrandXpath).extract()
        Brand = self.getAtribute(Brand, 'Производитель')
        Artikul = response.xpath(self.artikulXpath).extract()
        Artikul = self.getAtribute(Artikul, 'Артикул')
        Code = response.xpath(self.codelXpath).extract()
        Code = self.getAtribute(Code, 'Код товара')
        Country = response.xpath(self.countryXpath).extract()
        Country = self.getAtribute(Country, 'Страна')
        Description = response.xpath(self.descriptionXpath).extract_first().strip()

        item = DentalItem()
        item['Title']        = Title
        item['Price']        = Price
        item['Brand']        = Brand
        item['Artikul']      = Artikul
        item['Code']         = Code
        item['Country']      = Country
        item['Description']  = Description

        print(item, response.url)
        yield item


    def getAtribute(self, html, atribute):
        soup = BeautifulSoup(html[0], 'lxml')
        Atribute = soup.find('td', text = re.compile(atribute))
        try:
            Atribute = Brand.parent.findAll('td')[1].text
        except:
            Atribute = atribute + ': нет'
        return Atribute
