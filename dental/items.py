# -*- coding: utf-8 -*-


import scrapy


class DentalItem(scrapy.Item):

    Title       = scrapy.Field()
    Price       = scrapy.Field()
    Brand       = scrapy.Field()
    Artikul     = scrapy.Field()
    Code        = scrapy.Field()
    Country     = scrapy.Field()
    Description = scrapy.Field()
