# -*- coding: utf-8 -*-
import scrapy

class ZjgsSpider(scrapy.Spider):
    # 总局
    name = "zjgs"
    allowed_domains = ["gsxt.saic.gov.cn"]
    start_urls = (
        'http://gsxt.saic.gov.cn/zjgs/search/ent_except_list',
    )


    def parse(self, response):
        name = response.xpath('//table[@class="list-table"]/tr/td[1]/a/text()').extract()
        ID   = response.xpath('//table[@class="list-table"]/tr/td[2]/text()').extract()
        date = response.xpath('//table[@class="list-table"]/tr/td[3]/text()').extract()
        for i in xrange(len(name)):
            print name[i]
            print ID[i]
            print date[i]
            print "*"*20
        pass