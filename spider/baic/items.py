# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaicRecordItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 登记信息
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


    # 备案信息
    person_id   = scrapy.Field()
    person_name = scrapy.Field()
    person_post = scrapy.Field()
    
    # 经营异常信息
    Abnormal_ID  = scrapy.Field()
    Abnormal_reson = scrapy.Field()
    Abnormal_time = scrapy.Field()
    Abnormal_remove = scrapy.Field()
    Abnormal_remove_date = scrapy.Field()
    Abnormal_remove_auth = scrapy.Field()