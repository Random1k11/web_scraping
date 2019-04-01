import scrapy




class DentalFirstSpider(scrapy.Spider):

    name = 'dental'
    start_urls = ['https://dental-first.ru/']
    allowed_domains = ['https://dental-first.ru/']

    def __init__(self):
        self.declare_xpath()

    def declare_xpath(self):
        self.main_menuXpath = '//div[@class="box-catalog-list"]/ul/li/a/@href'
        self.sub_menuXpath = "//ul[@class='bx_catalog_line_ul']/li/a/@href"
        self.TitleXpath  = "//div[@class='list_list_p']/span/text()"
        self.priceXpath = "//div[@class='list_list_p']/font/text()"
        self.artikulXpath = "//table[@class='tabletable']//tbody/tr[1]"
        self.BrandXpath = "//table[@class='tabletable']//tbody/tr[2]"
        self.countryXpath = "//table[@class='tabletable']//tbody/tr[3]"
        self.descriptionXpath = "//div[@class='bx_item_description']"


    def parse(self, response):
        for menu in response.xpath(self.main_menuXpath):
            url = 'https://dental-first.ru' + menu.extract()
            print(url)
            yield scrapy.Request(url, callback=self.parse_main)



    def parse_main(self,response):
        print(123)

    # def parse_sub_menu(self, response):
    #     print(333)
    #     for sub_menu in response.xpath(self.sub_menuXpath):
    #         url = 'https://dental-first.ru' + sub_menu.extract()
    #         # print(url, '@@@')
    #         # yield scrapy.Request(url)



    def parse_main_item(self, response):

        main_menu = response.xpath(self.main_menuXpath).extract()

        sub_menu = response.xpath(self.sub_menuXpath).extract()
        price = response.xpath(self.priceXpath).extract()
        artikul = response.xpath(self.artikulXpath).extract()




        item['Title']          = Title
        item['Price']          = Price
        item['Brand']          = Brand
        item['CodeProduct']    = CodeProduct
        item['CodeProducer']   = CodeProducer
        item['Description']    = Description

        yield item
