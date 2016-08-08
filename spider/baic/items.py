# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaicRecordItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url  = scrapy.Field()
    city = scrapy.Field()
    register_ID   = scrapy.Field()
    register_name = scrapy.Field()
    type = scrapy.Field()
    representative = scrapy.Field()
    capital = scrapy.Field()
    establishment = scrapy.Field()
    lodgment = scrapy.Field()
    Operating_start = scrapy.Field()
    Operating_end   = scrapy.Field()
    Business_scope  = scrapy.Field()
    reg_authority = scrapy.Field()
    Approved_date = scrapy.Field()
    status = scrapy.Field()
