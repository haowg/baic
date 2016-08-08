# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
import time
class BJSpider(scrapy.Spider):
    # 北京
    name = "bj"
    allowed_domains = ["gov.cn"]
    start_urls = (
        'http://qyxy.baic.gov.cn/dito/ditoAction!ycmlFrame.dhtml?clear=true',
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
            next_page = self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li/a[@onclick="nextPage()"]')
        except Exception, e:
            print e

        while next_page:
            try:
                self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li/a[@onclick="nextPage()"]').click()
            except Exception, e:
                print e
                pass
            self.driver.current_window_handle
            aa = self.driver.page_source
            body = Selector(text=aa)
            name = body.xpath('//table[@class="ccjcList"]/tr/td[1]/a/text()').extract()
            ID   = body.xpath('//table[@class="ccjcList"]/tr/td[2]/text()').extract()
            date = body.xpath('//table[@class="ccjcList"]/tr/td[3]/text()').extract()
            for i in xrange(len(name)):
                print name[i]
                print ID[i]
                print date[i]
                print "*" * 20

            time.sleep(5)
            next_page = self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li/a[@onclick="nextPage()"]')
        pass