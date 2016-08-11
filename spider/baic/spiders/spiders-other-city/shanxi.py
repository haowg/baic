# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
import time


class SXSpider(scrapy.Spider):
    # 山西
    name = "shanxi"
    allowed_domains = ["gov.cn"]
    start_urls = (
        'http://gsxt.fc12319.com/exceptionInfoSelect.jspx',
    )
    # 初始化，这里要调用无头浏览器
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:8080/wd/hub',
            desired_capabilities={
                'takeScreenshot': False,
                'javascriptEnabled': True,

        })

    def parse(self, response):
        self.driver.get(response.url)
        try:
            next_page = self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li[12]/a')

        except Exception as e:
            print e
        while next_page:
            aa = self.driver.page_source
            body = Selector(text=aa)
            name = body.xpath('//div[@style="height:600px;"]/div/ul/li[1]/a/text()').extract()
            ID   = body.xpath('//div[@style="height:600px;"]/div/ul/li[2]/text()').extract()
            date = body.xpath('//div[@style="height:600px;"]/div/ul/li[3]/text()').extract()
            for i in xrange(len(ID)-1):
                print name[i]
                print ID[i+1]
                print date[i+1]
                print "*" * 20
                time.sleep(5)
            try:
                self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li[12]/a').click()
                self.driver.current_window_handle
            except Exception, e:
                print e
            next_page = self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li[12]/a').is_enabled()
