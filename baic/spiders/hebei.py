# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
import time
class HeBSpider(scrapy.Spider):
    # 山西
    name = "hebei"
    allowed_domains = ["gov.cn"]
    start_urls = (
        'http://www.hebscztxyxx.gov.cn/notice/search/ent_except_list',

    )
    # 初始化，这里要调用无头浏览器
    def __init__(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:8080/wd/hub', desired_capabilities={
            'takeScreenshot': False,
            'javascriptEnabled': True,

        })

    def parse(self, response):
        self.driver.get(response.url)
        try:
            next_page = self.driver.find_element_by_xpath('//div[@class="list-stat"]/div/ul/li[13]/a')
            # print  next_page
        except Exception, e:
            print e

        while next_page:
            aa = self.driver.page_source
            body = Selector(text=aa)
            name = body.xpath('//table[@class="list-table"]/tr/td[1]/a/text()').extract()
            ID   = body.xpath('//table[@class="list-table"]/tr/td[2]/text()').extract()
            date = body.xpath('//table[@class="list-table"]/tr/td[3]/text()').extract()
            for i in xrange(len(ID)):
                print name[i]
                print ID[i]
                print date[i]
                print "*" * 20
                time.sleep(5)
            try:
                self.driver.find_element_by_xpath('//div[@class="list-stat"]/div/ul/li[13]/a').click()
                self.driver.current_window_handle
            except Exception, e:
                print e
                pass
            next_page = self.driver.find_element_by_xpath('//div[@class="list-stat"]/div/ul/li[13]/a').is_enabled()
        pass