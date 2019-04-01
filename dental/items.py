# -*- coding: utf-8 -*-


import scrapy


class DentalItem(scrapy.Item):

    Title             = scrapy.Field()
    Price             = scrapy.Field()
    Brand             = scrapy.Field()
    Artikul           = scrapy.Field()
    Code              = scrapy.Field()
    Country           = scrapy.Field()
    Description       = scrapy.Field()
    Main_section      = scrapy.Field()
    Sub_section       = scrapy.Field()
    Under_sub_section = scrapy.Field()
    Href              = scrapy.Field()
